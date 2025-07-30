# https://www.codingame.com/training/easy/ascii-art-the-drunken-bishop-algorithm

W, H = 17, 9
S = (8, 4)
MOVES = {"00": (-1, -1), "01": (1, -1), "10": (-1, 1), "11": (1, 1)}
SYMBOLS = {
    0: " ",  1: ".",  2: "o",  3: "+",  4: "=",  5: "*",  6: "B",  7: "O",  8: "X",  9: "@",
    10: "%", 11: "&", 12: "#", 13: "/", 14: "^",
}

fingerprint = input().split(":")
instructions = []
for byte in fingerprint:
    data = bin(int(byte, 16))[2:].zfill(8)
    for shift in (6, 4, 2, 0):  
        instructions.append(data[shift:shift+2])

grid = [[0] * W for _ in range(H)]
bishop = S

for instruction in instructions:
    x, y = bishop
    dx, dy = MOVES[instruction]
    x = x + dx if  0 <= x + dx < W else x
    y = y + dy if 0 <= y + dy < H else y
    bishop = (x, y)
    grid[y][x] += 1

print("+---[CODINGAME]---+")
for y in range(H):
    row = ""
    for x in range(W):
        if (x, y) == S:
            row += "S"
        elif (x, y) == bishop:
            row += "E"
        else:
            row += SYMBOLS[grid[y][x] % len(SYMBOLS)]
    print(f"|{row}|")
print("+-----------------+")
