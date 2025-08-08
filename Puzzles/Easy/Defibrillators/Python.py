# https://www.codingame.com/training/easy/defibrillators

import math

lon, lat, n, o = float(input().replace(",", ".")), float(input().replace(",", ".")), int(input()), ("", float("inf"))
for i in range(n):
    _, name, _, _, lo, la = input().split(";")
    lo, la = float(lo.replace(",", ".")), float(la.replace(",", "."))
    x = (lo - lon) * math.cos((lat + la)/2)
    y = la - lat
    d = math.sqrt(x*x + y*y) * 6371
    if d < o[1]:
        o = (name, d)
print(o[0])
