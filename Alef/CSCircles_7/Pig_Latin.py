# Outputs the Input in Pig Latin by moving the first letter to the end and adding "ay"

s = input()

s_first = s[0]

print(s[1:len(s)] + s_first + "ay")
