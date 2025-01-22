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

 ------------------------------------------------------------------------------------
# Word Scramble
import random
words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]

# Define word scramble function
def word_scrambled(word):                       
    word_scrambled = ''.join(random.sample(word, len(word)))
    return word_scrambled

while True:
    select_word = random.choice(words) #select the word and scramble it
    guess = input("Guess the Word: " + word_scrambled(select_word)) 

# Check if the guess is correct
    if guess == select_word: 
        print("Your guess is correct")
        break
    else:
        print("Wrong guessing")

# Allow the user to continue or quit
    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        print("Thank you for playing!")
        break
