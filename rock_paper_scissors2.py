# rock = 0, paper = 1, scissors = 2
import random

fullname = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}
bot = ['r', 'p', 's'] # 0:r, 1:p, 2:s

player = input("Rock [r], Paper [p], Scissors [s]: ")
print("You choose:", fullname[player])

botChoose = bot[random.randint(0, 2)]
print('Bot:', fullname[botChoose])

decision = player+botChoose

winner = ''

if decision == 'rs' or decision == 'pr' or decision == 'sp':
    winner = 'Player'
elif decision == 'rp' or decision == 'ps' or decision == 'sr':
    winner = 'Bot'
else:
    winner = 'Draw'

print("The winner is the", winner)