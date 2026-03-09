# Number Guessing Game

import random  

print(" Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 50. Can you guess it?")

secret_number = random.randint(1, 50) # Generate random number between 1 and 50

attempts = 0 #Initialize attempts counter

while True: #Loop until user guesses correctly
    guess = input("Enter your guess: ")
    
    guess = int(guess)
    
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again 🔽")

    elif guess > secret_number:
        print("Too high! Try again 🔼")
        
    else:
        print(f"🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
        break  # Exit loop when guessed correctly

print("Thanks for playing the Number Guessing Game!")