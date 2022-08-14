coins = input('Enter coins combination (use 0 or 1): ')
tails = 0
for side in coins:
    if int(side):
        tails += 1
heads = len(coins) - tails

print(f'{tails if tails < heads else heads} flips')