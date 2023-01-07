import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# import random
#
# number = random.ranint(1, 10)
# print(number)

# import random
#
# coin = random.choice(["heads", "tails"])
# print(coin)

# from random import choice  # Gets a function from a module
#
# coin = choice(["heads", "tails"])  # Don't need to call random, "choice" works
# print(coin)
