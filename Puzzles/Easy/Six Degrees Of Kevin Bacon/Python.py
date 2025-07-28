# https://www.codingame.com/training/easy/six-degrees-of-kevin-bacon

from collections import deque

def bfs(t, a):
    vtd = []
    que = deque([(a, 0)])
    while que:
        act, dst = que.popleft()
        if act == "Kevin Bacon":
            return dst
        if act not in vtd:
            vtd.append(act)
            for nbr in t.get(act, []):
                if nbr not in vtd:
                    que.append((nbr, dst + 1))

act = input()
n = int(input())
cst = {}
for i in range(n):
    c = input().split(": ")
    cst[c[0]] = c[1].split(", ")

tr = {}
for mov in cst:
    for act1 in cst[mov]:
        for act2 in cst[mov]:
            if act1 == act2:
                continue
            if act1 not in tr:
                tr[act1] = []
            if act2 not in tr[act1]:
                tr[act1].append(act2)

print(bfs(tr, act))
