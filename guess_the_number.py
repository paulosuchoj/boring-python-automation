import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of  a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')

    try:
        guess = int(input())
        
        if guess < secretNumber:
            print('That is too low. Try again.')
        elif guess > secretNumber:
            print('That is too high. Try again.')
        else:
            break
    except ValueError:
        print('Please guess only numbers, not letters or symbols.')

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' tries.')
else:
    print('No. The number I was thinking of was ' + str(secretNumber))
          
