# Mubashir.py

def mubashir_cipher(message):
    # List
    key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], 
    ['s', 'v'], ['h', 'x'], ['i', 'z'], ['r', 'y'], 
    ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]

    encode = ''
    for letter in message:
        found = False
        for k in key:
            if letter == k[1]:
                encode += k[0]
                found = True

            elif letter == k[0]:
                encode += k[1]
                found = True

        if not found:
            encode += letter
    
    print(encode)


mubashir_cipher("mubashir is not amazing")
