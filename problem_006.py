def sum_of_squares(n):
    total = 0
    for i in range(1,n+1):
        total += i**2
    return total

def square_of_sum(n):
    total = 0
    for i in range(1,n+1):
        total += i
    total = total**2
    return total

print(square_of_sum(100)-sum_of_squares(100))
