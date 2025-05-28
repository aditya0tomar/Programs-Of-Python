def factorial(n):
    if n==0:
      return 1 # Base case: factorial of 0 is 1
    else:
      return n * factorial (n-1)# Recursive case: n! = n * (n-1)!
print(factorial(5)) 
print(factorial(10)) 
print(factorial(6)) 
print(factorial(0)) 