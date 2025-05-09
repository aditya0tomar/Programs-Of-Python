#wap to print the sort order of given elements in list
'''a=[456,322,490,765,306]
a.sort()
print(a)'''
#WAP TO MAKE PROGRAMME OF USER DEFINE LIST AND SORT IT
l=[]
a=int(input("enter how many elements you want store in list"))
for i in range(0,a):
    b=int(input("enter values"))
    l.append(b)
print(l)
print("if i sort the list then our output is")
l.sort()
print(l)