from math import sqrt

number = 600851475143
#we can remove even factors
while number % 2 == 0:
    number /= 2
    print(number)
#now check odd factors
#factors naturally come in pairs so we only need to check to sqrt of number
for i in range (3, int(sqrt(number)) ,2):
    while number % i == 0 and number != i:
        number //= i
        print(number)














