import random


def guess(x):

    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Guess again , To low")
        elif guess > random_number:
            print("Guess again , To high")

    print(f"Good correct answer {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also between low = high
        feedback = input(f"is {guess} to high, to low, or correct :").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f'Your answer is {guess}')
#123123

computer_guess(100)