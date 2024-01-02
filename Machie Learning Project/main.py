import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier

# Fetch historical data for S&P 500
sp500 = yf.Ticker("^GSPC")
sp500_data = sp500.history(period="max")

# Print the first few rows of the DataFrame and the index
print(sp500_data.head())
print(sp500_data.index)

# Delete unnecessary columns
del sp500_data["Dividends"]
del sp500_data["Stock Splits"]

# Create a new column for tomorrow's closing prices
sp500_data["Tomorrow"] = sp500_data["Close"].shift(-1)

# Create a binary target column based on the condition
sp500_data["Target"] = (sp500_data["Tomorrow"] > sp500_data["Close"]).astype(int)

# Print the relevant columns including "Target"
print(sp500_data[["Close", "Tomorrow", "Target"]].head())

# Filter data from 1990-01-01 onwards
sp500_data = sp500_data.loc["1995-01-01":].copy()
print(sp500_data)

# Corrected column name in predictors
predictors = ["Close", "Volume","Open", "High", "Low"]

# Handling missing values if any
sp500_data.dropna(inplace=True)

# Split the data into training and testing sets
train = sp500_data.iloc[:-100]
test = sp500_data.iloc[-100:]

# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

# Train the model
model.fit(train[predictors], train["Target"])

# Make predictions on the test set
test.loc[:, "Predictions"] = model.predict(test[predictors])

from sklearn.metrics import precision_score

precisionscore = model.predict(test[predictors])
precisionscore = pd.Series(precisionscore, index=test.index)

print("This is the", precisionscore)



# Plot the closing prices and predictions
plt.plot(test.index, test["Close"], label="Actual Closing Prices", color='blue')
plt.plot(test.index, test["Predictions"], label="Predicted Closing Prices", color='red')
plt.title('S&P 500 Actual vs Predicted Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()
