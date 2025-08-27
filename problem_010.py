#this is slow but answer is correct
from math import sqrt
primes = []
for x in range(2,2000000):
    prime = True
    for y in range(2,int(sqrt(x)+1)):
        if x % y == 0:
            prime = False
            break
    if prime:
        primes.append(x)

sums = 0

for z in primes:
    sums += z

print(sums)