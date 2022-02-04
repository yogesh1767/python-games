import random

def guess(x):
    random_number = random.randint(1, x) #randint generate random number(start, end)
    guess =0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('please guess again. Too low')
        elif guess > random_number:
            print('guess again. Too high')

    print(f'Dear user, youu have guessed the number {random_number} correctly')

guess(10) 
