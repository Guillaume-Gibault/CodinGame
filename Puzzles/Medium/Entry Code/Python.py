# https://www.codingame.com/training/medium/entry-code

x = int(input())
n = int(input())

def dfs(v):
    for d in digits:
        e = v + d
        if e not in seen:
            seen.add(e)
            dfs(e[1:])
            path.append(d)

digits = list(map(str, range(x)))
zero = "0"*(n-1)
seen = set()
path = []
dfs(zero)
print(zero + "".join(reversed(path)))
