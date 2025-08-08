# https://www.codingame.com/training/easy/button-mash

i = int(input())
o = 0
while i > 0:
    if i % 2 == 0:
        i /= 2
    else:
        if i != 3 and (i + 1) % 4 == 0:
            i += 1
        else:
            i -= 1
    o += 1
print(o)
