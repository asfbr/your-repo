import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(94):
        if flips[i] == flips[i + 1] == flips[i + 2] == flips[i + 3] == flips[i + 4] == flips[i + 5]:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 100))
