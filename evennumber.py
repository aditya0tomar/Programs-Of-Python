#WAP TO CHECK THE GIVEN NUMBER IS EVEN OR NOT
'''num=int(input("enter the num which you want to check its even or not = "))
if (num%2==0):
    print(num,"is even number")
else:
    print("it is not even number")
'''
#WAP TO CHECK THE WHICH NUM IS EVEN WHEN I HAVE MANY  NUMBERS
A = [3, 5, 4, 22, 12, 46, 8]
A.sort()
print("Sorted list:", A)

even_numbers = []

for num in A:
    if num % 2 == 0:
        even_numbers.append(num)

if even_numbers:
    for num in even_numbers:
        print(f"{num} is divisible by 2")
else:
    print("No number is divisible by 2")
