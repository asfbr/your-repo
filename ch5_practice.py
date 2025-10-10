import random

# Get the user's first guess
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# Perform the coin toss and convert the result to a string
toss_integer = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss_integer == 1:
    toss_result = 'heads'
else:
    toss_result = 'tails'

# Compare the user's guess with the string result
if guess == toss_result:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()  # Get the second guess
    if guess == toss_result:
        print('You got it!')
    else:
        print(f"Nope. The toss was {toss_result}. You are really bad at this game.")