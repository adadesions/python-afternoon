text = "Hello, Ada"

encode = ''
decode = ''
shift = 1

print("original text:", text)

# Encode Section
for t in text:
    x = ord(t) + shift
    encode += chr(x)

print('Encode text:', encode)

# Decode Section
for e in encode:
    x = ord(e) - shift # number
    decode += chr(x) # character

print('Decode text:', decode)

