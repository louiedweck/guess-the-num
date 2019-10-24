import random

print('Hello! What is your name?')
my_name = input()

guess = int(
    input(f"Hi {my_name}, I'm thinking of a number from one to 100, can you guess what it is? "))

num_of_tries = 1
computer_guess = random.randint(0, 100)
while guess is not computer_guess:
    num_of_tries += 1
    if guess < computer_guess:
        print("Your guess is too low. Try a higher one!")
    elif guess > computer_guess:
        print("Your guess it too high. Try a lower one!")
    guess = int(input("Have another guess?"))

print(f"Nice job {my_name}, it took you, {num_of_tries} tries")
