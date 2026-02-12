width = int(input())

while True:
    string = input()

    if string == "END":
        break

    period_count = width - len(string)
    left = period_count // 2 + (period_count % 2)
    right = period_count // 2

    print("." * left + string + "." * right)
