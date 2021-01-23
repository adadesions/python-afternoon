# Stuttering.py

def stutter(word):
    two_letters = word[:2]
    
    print(f'{two_letters}... {two_letters}... {word}?')


stutter('incredible')
stutter('Arkane')
stutter('Outstanding')
