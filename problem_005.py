#brute force method
def divisible_all(n):
    for i in range(20, 0, -1 ):
        if n % i != 0:
            return False
    return True

#start from 20 as must be divisible by 20
for number in range(20,1000000000000, 20):
    if divisible_all(number):
        print(number)
        break

#Lowest common multiple, importing math
import math
LCM = 1
for x in range(1,21):
    LCM = math.lcm(LCM, x)
print(LCM)
