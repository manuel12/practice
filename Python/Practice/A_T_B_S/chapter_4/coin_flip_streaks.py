import random
num_streaks = 0
head_or_tails = []


# Code that creates a list of 100 heads or tail values.
head_or_tails = ['H' if random.randint(0,1) == True else 'T' for index in range(10000)]
heads = "".join(head_or_tails).count('HHHHHH')
tails = "".join(head_or_tails).count('TTTTTT')

num_streaks =  heads + tails
print('Chance of streak in a row: %s%%' % (num_streaks / 100))

