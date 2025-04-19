
fib = [0, 1]

for i in range(2, 100):  # 100 is a safe limit
    next_fib = fib[i - 1] + fib[i - 2]
    if next_fib > 500:
        break
    fib.append(next_fib)

print("Fibonacci numbers between 0 and 500:", fib)
print("Total count:", len(fib))