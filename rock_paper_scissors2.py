# rock = 0, paper = 1, scissors = 2
import random

fullname = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}
bot = ['r', 'p', 's'] # 0:r, 1:p, 2:s
score = {
    'player': 0,
    'bot': 0,
    'draw': 0
}

while True:
    player = input("Rock [r], Paper [p], Scissors [s], Exit [x]: ")

    if player == 'x':
        print("Thanks for playing, see ya next time!")
        print("===== Score Board =====")
        print("Player:",score['player'])
        print("Bot:",score['bot'])
        print("Draw:",score['draw'])
        print("=======================")
        print("The Champion: ", "Player" if score['player'] > score['bot'] else 'Bot')
        print("=======================")

        break

    if len(player) > 1:
        continue
    
    if player not in 'rsp' or player == '':
        continue

    print("You choose:", fullname[player])
    botChoose = bot[random.randint(0, 2)]
    print('Bot:', fullname[botChoose])

    decision = player+botChoose

    winner = ''

    if decision == 'rs' or decision == 'pr' or decision == 'sp':
        winner = 'Player'
        score['player'] += 1
    elif decision == 'rp' or decision == 'ps' or decision == 'sr':
        winner = 'Bot'
        score['bot'] += 1
    else:
        winner = 'Draw'
        score['draw'] += 1

    print("The winner is the", winner)