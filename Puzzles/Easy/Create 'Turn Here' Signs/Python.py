# https://www.codingame.com/training/easy/create-turn-here-signs

DIR = {"left": "<", "right": ">"}

d, *p = input().split()
n, h, t, s, i = map(int, p)

for r in (range(h) if d == "right" else range(h // 2, h + h // 2)):
    print((" "*i)*(r if r < h/2 else abs(h - r - 1)), end="")
    for c in range(n):
        print(DIR[d]*t, end="")
        if c != n-1:
            print(" "*s, end="")
    print()
