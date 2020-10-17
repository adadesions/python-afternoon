# Random an imposter!
import random

num_players = int(input("Enter players number: "))
players = [0] * num_players

num_imposter = int(input("Enter imposter number: "))
imposters = []

for i in range(num_imposter):
    x = random.randint(0, num_players - 1)

    if x in imposters:
        x = random.randint(0, num_players - 1)

    imposters.append(x)

print('Before random an imposter:', players)

for i in imposters:
    players[i] = 1

print('After random an imposter:', players)
