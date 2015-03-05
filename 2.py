fibsum = 0
fib1 = 0
fib2 = 1
while (fib2 < 4000000):
    if (fib2 % 2) == 0:
        fibsum += fib2
    temp = fib1
    fib1 = fib2
    fib2 = temp + fib2
print fibsum
