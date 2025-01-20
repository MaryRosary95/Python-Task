#Guess the Number
import random
computer_guess = random.randint(1, 10)
while True:
    my_guess = int(input())

    if my_guess < computer_guess:
        print("Too High, Try with different number")
    elif my_guess > computer_guess:
        print("Too low, Try with different number")
    else:
        print("Your guess is correct")
        break


    