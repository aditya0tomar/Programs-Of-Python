#WAP to print the which dict value has max attribute in given list and print with clearification
'''a=[{1:2,3:9},{"abc":1,"xyz":2,"mno":3},{25:63}]
d1=(a[0])#HERE WE REMOVE OUR DICT FROM LIST
d2=(a[1])
d3=(a[2])
l1=(list(d1))#WITH TYPE CONVERSING I CONVERT ALL DICT INTO LIST
l2=(list(d2))
l3=(list(d3))
print(l1,l2,l3)
total_elementsl1=len(l1)#NOW COUNT THE ELEMENTS OF EVERY LISTz
total_elementsl2=len(l2)
total_elementsl3=len(l3)
#NOW WE HAVE TO FIND WHICH LIST HAS MAX ELEMENTS
if (total_elementsl1>total_elementsl2 and total_elementsl1>total_elementsl3):
    print("l1 has max elements in given list")
elif (total_elementsl2>total_elementsl3 and total_elementsl2>total_elementsl1):
    print("l2 has max elements in given list")
elif (total_elementsl3>total_elementsl2 and total_elementsl3>total_elementsl1):
    print("l3 has max elements in given list")
else:
    print("sorry you are wrong some where")'''

#WAP TO TAKE KEY AND VALUE FROM USER AND STORE INN DICT AND TELL US HOW MANY elements of pair in dict
'''d={}
A=int(input("Hoe many elements of pair you want put in dict=="))
for i in range(A):
    key=input("enter your key =")
    value=input("enter your value =")
    d[key]=value
print(d)
print("number of pair elements in dict",len(d))'''
#wap to print the mupltiply of paired by paired by number in tuple
'''t=(3,7,4,9,5,7,6)
a=t[0]*t[1],t[1]*t[2],t[2]*t[3],t[3]*t[4],t[4]*t[5],t[5]*t[6]
print(a)'''
#WAP of below programee at taking from user
'''l = []
f = int(input("How many elements you want to put in tuple: "))
for i in range(f):
    j = int(input(f"Enter value {i+1}: "))
    l.append(j)
t = tuple(l)
print("Your tuple is:", t)
multiplications = []
for i in range(len(t)-1):
    multiplications.append(t[i] * t[i+1])
print("Multiplication of elements in pair is:", tuple(multiplications))
#WAP TO PRINT THE CUBE 
l=[2,3,4,5]
print(l**2)'''

