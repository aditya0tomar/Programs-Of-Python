while True:
    def add(x,y):#HERE WE CREATE A FUNC OF EVERY OPERATOR 
      return x + y
    def subtract(x,y):
      return x - y
    def multiply(x,y):
       return x * y
    def divide(x,y):
       return x / y
 
 
    print("please select operation what you want to do")#HERE I ASK TO USER WHAT SHOULD I DO FOR YOUR CALCULATION

    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. dividion")

    choice=input("Dude Enter your choice: \1\2\3\4")#HERE USER ORDER ME WHAT HE WANT TO DO

    num1=float(input("enter first number"))#TAKE 2 NUMBERS AS INPUT
    num2=float(input("enter second number"))
    
    print("HEY USER YOUR GIVEN COMMAND IS DONE AND YOUR ANSWER IS")#THIS IS NORMAL MSG FOR IMPRESSIVE LOOK

    if choice == '1':#FROM HERE WE RUN THE IF ELIF ELSE CONDITION
        print("result:" , add(num1,num2))
    if choice == '2':
        print("result:" , subtract(num1,num2))
    elif choice == '3':
        print("result:" , multiply(num1,num2))
    elif choice == '4':
        print("result:" , divide(num1,num2))
    else:
        print=("invalid output")
    