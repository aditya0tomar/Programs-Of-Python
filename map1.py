#these all are some complicated method of when we have to find of all elements that stored in list
'''def cube(x):
    return x*x*x
l=[3,4,5,6,7,9]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)'''
#we can increase our compelexity from map method
'''def cube(x):
    return x*x*x

l=[3,5,6,3,1,7,8,9]
newl=[]
newl=list(map(cube,l))
print(newl)
print(cube(90))#these all are simple method for when we have to give onl 2 value at a time
print(cube(91))
print(cube(92))
print(cube(93))'''
#same things happening with lambda
'''numbers = [1,2,3,4,5,6,7,8,9,10]
squared = map(lambda x: x*x*x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]'''
#programme of when we have to define grades with help   of map
l = [78, 54, 90, 84, 59, 90, 76, 68]  # Fixed double comma

def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

graded = list(map(grade, l))
print(graded)

