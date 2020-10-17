# Secrete Message
text = "Hello Ada"

# Dictaionary
table = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5
}

sample = "abc"
shift = 1
cipher = ''
decode_text = ''

print("Original text:", sample)
for s in sample:
    encode = table[s] + shift
    keys = list(table.keys())
    cipher += keys[encode]

print("Cipher text:", cipher)
for c in cipher:
    decode = table[c] - shift
    keys = list(table.keys())
    decode_text += keys[decode]

print("Decode text:", decode_text)

# https://github.com/adadesions/python-afternoon