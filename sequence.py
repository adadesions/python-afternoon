# 1, 1, 2, 3, 5, 8, 13, 21, 34,...

a1 = 1
a2 = 2
an = a1 + a2
print(a1, ',', a2, end=", ")
sum = 0
for n in range(100):
    an = a1 + a2

    if an > 4000000:
        print("=== Done ===")
        break
    if an % 2 == 0:
        sum += an
        print(an, end=", ")

    a1 = a2
    a2 = an

print("even-sum =", sum)
