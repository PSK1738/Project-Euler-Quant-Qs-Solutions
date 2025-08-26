number = 600851475143
while number % 2 == 0:
    number /= 2
    print(number)

for i in range (3, 600851475143 ,2):
    while number % i == 0 and number != i:
        number //= i
        print(number)
