# https://www.codingame.com/training/easy/mars-lander-episode-1

surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    rot = 0
    pwr = 0
    if 0 < v_speed < -5:
        pwr = 3
    elif v_speed < -20:
        pwr = 4
    print(f"{rot} {pwr}")
