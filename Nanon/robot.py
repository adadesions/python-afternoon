name = input("What's your name? : ")
print("How are you,", name, "?")

age = input("How old are you? : ")
age = int(age)
print(name, "is", age, "years old")

if age > 50:
    print("You're too old!")
else:
    print("You're still young")