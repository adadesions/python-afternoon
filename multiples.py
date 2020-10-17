#  n < 1000 and 3 | n or 5 | n
# sum all n
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        sum += i
print("sum =", sum)