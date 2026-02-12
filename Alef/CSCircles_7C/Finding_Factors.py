n = int(input())

for a in range(1, n + 1):
    if n % a == 0:
        b = n // a
        print(a, "times", b, "equals", n)

