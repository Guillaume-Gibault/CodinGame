# https://www.codingame.com/training/easy/ascii-art

l = int(input())
h = int(input())
t = input().upper()

alphabet = {}
for i, letter in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ?")):
    alphabet[letter] = i

for i in range(h):
    line = ""
    ascii = input()

    for char in list(t):
        if char.isalpha():
            offset = alphabet[char] * l
        else:
            offset = alphabet["?"] * l

        line += str(ascii[offset:offset+l])
    print(line)
