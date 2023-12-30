# Check for even
print("Below given are for even numbers")
my_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for num in my_iterable:
    if num % 2 == 0:
        print(f'Even number: {num}')
    else:
        print(f'Odd number: {num}')
list_sum = 0

for num in my_iterable:
    list_sum = list_sum + num
    print(list_sum)
    
mylist = [(1,2),(3,4),(5,6),(6,7)]

print(len(mylist))

for item in mylist:
    print(item)