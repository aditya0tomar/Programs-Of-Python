import random
#GENERATE A RANDOM NUMBER BETWEEN 1 AND 10
secret_number = random.randint(1,10)
#ASK THE USER TO GUESS
guess = int (input("guess a number between 1 to 10 ="))
#check the guess
if guess == secret_number:
    print("congrats dude ! you guessed it right =")
else:
    print(f"sorry the correct number was {secret_number}..try again!")