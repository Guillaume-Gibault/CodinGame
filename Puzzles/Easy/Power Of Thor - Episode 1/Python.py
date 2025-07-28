# https://www.codingame.com/training/easy/power-of-thor-episode-1

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x = initial_tx
y = initial_ty

# game loop
while True:
    remaining_turns = int(input())
    out = ""
    if light_y > y and not y+1 > 17:
        out += "S"
        y += 1
    elif light_y < y and not y-1 < 0:
        out += "N"
        y -= 1
    if light_x > x and not x+1 > 39:
        out += "E"
        x += 1
    elif light_x < x and not x-1 < 0:
        out += "W"
        x -= 1
    print(out)
