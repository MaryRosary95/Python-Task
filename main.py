# Guess the Number
import random
computer_guess = random.randint(1, 10)         #Random Values of the system guess
while True:

    my_guess = int(input("Enter your input:")) #User providing the input

    if my_guess < computer_guess:              #Guessing loop starts
        print("Too High, Try with different number")
    elif my_guess > computer_guess:
        print("Too low, Try with different number")
    else:
        print("Your guess is correct")
        break

    
