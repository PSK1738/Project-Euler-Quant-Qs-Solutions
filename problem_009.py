from math import sqrt


def pyth(x, y):
    return sqrt(x ** 2 + y ** 2)


#originally was getting too many pairs as I wasn't checking if c was an integer. int() was flooring c.
for b in range(2, 1000):
    for a in range(1, b):
        if pyth(a,b).is_integer() and int(pyth(a, b)) + a + b == 1000:
            print(a, b, int(pyth(a, b)) )
            solution = a * b * int(pyth(a, b))
            print(solution)