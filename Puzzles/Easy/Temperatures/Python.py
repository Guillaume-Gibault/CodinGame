# https://www.codingame.com/training/easy/temperatures

n = int(input())  # the number of temperatures to analyse
t = []
for i in input().split():
    t.append(int(i))

if len(t) != 0:
    out = 5526
    for temp in t:
        if abs(temp) == abs(out):
            out = max(temp, out)
        elif abs(temp) < abs(out):
            out = temp
    print(out)
else:
    print(0)
