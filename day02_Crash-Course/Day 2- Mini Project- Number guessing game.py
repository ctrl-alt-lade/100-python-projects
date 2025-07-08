import random

secret_number = random.randint(1, 10)
attempts = 3

print("I'm thinking of a number between 1 and 10")

prompt = ("Take a Guess")
while attempts > 0:
    guess = int(input(prompt))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again. ")
    else:
        print("Too high! Try again. ")
    attempts -= 1 

if attempts == 0:
    print("oops! You've used up all your attempts. The secret number was: ", secret_number)