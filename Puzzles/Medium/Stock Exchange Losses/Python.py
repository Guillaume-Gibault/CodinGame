# https://www.codingame.com/training/medium/stock-exchange-losses

n = int(input())
val = []
for i in input().split():
    val.append(int(i))
max, res = 0, 0

for v in val:
    diff = v - max
    res = diff if diff < res else res
    max = v if v > max else max

res = 0 if res >= 0 else res
print(res)
