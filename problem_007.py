import math
from math import sqrt

primes = []

for number in range(2, 150000):
    prime = True
    for x in range(2, int(math.isqrt(number) + 1)):
        if number % x == 0:
            prime = False
            break
    if prime:
        primes.append(number)
        if len(primes) > 10001:
            break

print(primes[10000])
