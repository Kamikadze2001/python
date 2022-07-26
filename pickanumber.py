from random import randint

guesses = 0 
guess = 0
random = randint(1,9)

while guess != random and guess != 'exit':
    guesses += 1
    guess = input('Enter a number between 1-9 \n')
    guess = int(guess)
    if guess == 'exit':
        break

    if guess < random:
        print('to low')
    elif guess > random:
        print('To high')
    elif guess == random:
        print('You won! Number of ties ', guesses)
        break
