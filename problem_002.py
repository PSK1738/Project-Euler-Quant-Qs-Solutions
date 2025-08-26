fib_seq = [1, 2]
while fib_seq[-1] <= 4000000:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
fib_seq.pop()
total = 0
for i in fib_seq:
    if i % 2 == 0:
        total += i
print(total)