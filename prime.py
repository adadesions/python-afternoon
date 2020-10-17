# Defination of Prime
# If n is prime, 1 | n and n | n

def isPrime(n):
    for k in range(2, n):
        # print('k =', k)
        if n % k == 0:
            # print(k, '|', n)
            # print(n, 'is not a prime')
            return False
    # print(n, 'is a prime')
    return True

counter = 0
i = 2

while counter < 1000000:
    if isPrime(i):
        counter += 1
        print(i, 'is prime at', counter) 

    i += 1
