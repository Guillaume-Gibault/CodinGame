# https://www.codingame.com/training/easy/unary

i = str(input())
b, o = "", ""
for l in i:
    b += bin(ord(l))[2:].zfill(7)
for idx, n in enumerate(b):
    if n == "0":
        if idx > 1 and b[idx-1] == "0":
            o += "0"
        else:
            o += " 00 0"
    else:
        if idx > 1 and b[idx-1] == "1":
            o += "0"
        else:
            o += " 0 0"
print(o.strip())
