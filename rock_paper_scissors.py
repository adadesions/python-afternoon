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

winner = ''
if player == 'r' and botChoose == 'p':
    winner = 'Bot'
elif player == 'r' and botChoose == 's':
    winner  = 'Player'
elif player == 'p' and botChoose == 'r':
    winner = 'Player'
elif player == 'p' and botChoose == 's':
    winner = 'Bot'
elif player == 's' and botChoose == 'r':
    winner = 'Bot'
elif player == 's' and botChoose == 'p':
    winner = 'Player'
else:
    winer = 'Draw'
