# https://www.codingame.com/training/medium/remaining-card

import math

n = int(input())

m = math.floor(math.log2(n))
p = 2**m
l = n - p
o = n if l == 0 else 2*l
print(o)
