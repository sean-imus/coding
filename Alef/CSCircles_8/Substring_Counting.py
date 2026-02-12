needle = input()
haystack = input()

needle_times = 0
needle_length = len(needle)

for i in range(len(haystack) - needle_length + 1):
    if haystack[i:i+needle_length] == needle:
        needle_times += 1

print(needle_times)
