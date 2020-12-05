# PI Approximation
pi = 0
for n in range(10000000):
    pi += (-1)**n / (2*n + 1)

pi = 4*pi
print("PI =", pi)