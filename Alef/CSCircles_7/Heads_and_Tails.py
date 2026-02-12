# Outputs the Input with the first and last Character swapped

s = input()

s_first = s[0]
s_last = s[-1]

print(s_last + s[1:-1] + s_first)
