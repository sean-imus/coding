# Outputs the next Letter of the Alphabet assuming the Input is uppercase, loops on Z

s = input()

chr_num = ord(s)
next_chr = chr(chr_num + 1)

if chr(chr_num) == "Z":
    next_chr = "A"

print(next_chr)
