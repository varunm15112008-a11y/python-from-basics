import random


secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

while True:
    
    guess = int(input("Take a guess: "))

    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Good job! You guessed my number!")
        break  
