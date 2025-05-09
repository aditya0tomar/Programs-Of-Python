#complicated method
def cube(x):
    return x*x*x

l=[2,3,4,5,6,7]
newl=[]
for i in l:
    newl.append(cube(l))
print(newl)
