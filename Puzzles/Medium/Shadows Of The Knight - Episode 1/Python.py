# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1

w, h = [int(i) for i in input().split()]
n = int(input())
x, y = [int(i) for i in input().split()]
x_min, x_max, y_min, y_max = 0, w-1, 0, h-1

while True:
    dir = input()  # U, UR, R, DR, D, DL, L or UL

    if 'U' in dir:
        y_max = y - 1
    if 'D' in dir:
        y_min = y + 1
    if 'L' in dir:
        x_max = x - 1
    if 'R' in dir:
        x_min = x + 1

    x = (x_min + x_max) // 2
    y = (y_min + y_max) // 2

    print(f"{int(x)} {int(y)}")
