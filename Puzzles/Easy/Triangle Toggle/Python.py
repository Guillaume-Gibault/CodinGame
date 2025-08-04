# https://www.codingame.com/training/easy/triangle-toggle

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def in_triangle(p, p1, p2, p3):
    d1 = sign(p, p1, p2)
    d2 = sign(p, p2, p3)
    d3 = sign(p, p3, p1)
    neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (neg and pos)

h, w = [int(i) for i in input().split()]
style = input()
n = int(input())

triangles = []
grid = [["*"] * w for _ in range(h)]

for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if in_triangle((x,y), (x1,y1), (x2,y2), (x3,y3)):
                grid[y][x] = " " if grid[y][x] == "*" else "*"

for row in grid:
    if style == "expanded":
        print(" ".join(row))
    else:
        print("".join(row))
        