'''l = []
a = int(input("how many dictionary you want store in list: "))
b = int(input("Enter the number of key-value pairs in each dict: "))
for i in range(a):
    d = {}  # Create a new dictionary for each iteration
    for j in range(b):
        key = input("Enter your key: ")
        value = input("Enter your value: ")
        d[key] = value
    l.append(d)
print(l)'''
l = []
a = int(input("Enter the number of dictionaries you want to create: "))
for i in range(a):
    d = {}
    print(f"\nEntering data for dictionary {i+1}:")
    while True:
        key = input("Enter your key: ")
        value = input("Enter your value: ")
        d[key] = value

        more = input("Do you want to add another key-value pair? (yes/no): ").strip().lower()
        if more != "yes":
            break
    l.append(d)

print("\nFinal list of dictionaries:")
print(l)

