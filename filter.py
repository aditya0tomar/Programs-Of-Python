numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Output: [2, 4]
#basically this built in function used for filter the elmenets and which are useful for us give our output
l2=[4,5,6,7,8,9,10]
newl=filter(lambda y: y>5 ,l2)
print(list(newl))
 
