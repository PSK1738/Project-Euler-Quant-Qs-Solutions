#convert to string to find the palindrome
def palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

largest_palindrome = 0
#only record the largest as that's all we care about
for x in range(100,1000):
    for y in range(100,1000):
        result = x * y
        if palindrome(result):
            if result > largest_palindrome:
                largest_palindrome = result

print(largest_palindrome)