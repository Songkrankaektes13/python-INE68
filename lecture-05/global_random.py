import random

HEADS = 1
TAILS = 2
TOSSES = 10 # ตัวแปร คอนแซ้น

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

tosses_coin()