a=int(input("enter the number of element:"))
l=[]
for i in range(0,a):
    b=int(input("enter the number you want to put in element:"))
    c=(b,b**3)
    l.append(c)
d=tuple(l)
print(d)
