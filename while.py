x = 56

while x < 5:
    print(f'Current value of x is {x}')
    x = x + 1
else:
    print('X is not less than 5')


y = [1,2,3]

for item in y:
    pass
print('end of my script')

myname = 'sammy'

for letter in myname:
    if letter == 'a':
        continue
    print(letter)