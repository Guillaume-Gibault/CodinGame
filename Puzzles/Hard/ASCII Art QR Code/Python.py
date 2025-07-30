# https://www.codingame.com/training/hard/ascii-art-qr-code

W = int(input())
H = int(input())
grid = [list(input()) for _ in range(H)]

no_data_zone = [[False]*W for _ in range(H)]  # TL, TR & BL
for x, y in [(0, 0), (W - 6, 0), (0, H - 4)]:
    for dy in range(4):
        for dx in range(6):
            no_data_zone[y + dy][x + dx] = True

cross_zone = [row[:] for row in no_data_zone]  # BR
for dy in range(3):
    for dx in range(3):
        cross_zone[H - 4 + dy][W - 6 + dx] = True

data_coords = []
for i, x in enumerate(range(W - 1, -1, -1)):
    if i % 2 == 0:
        ys = range(H - 1, -1, -1)  # ↑
    else:
        ys = range(0, H)  # ↓
    for y in ys:
        if not cross_zone[y][x]:
            data_coords.append((y, x))

bitstream = []
for y, x in data_coords:
    raw = 0 if grid[y][x] == ' ' else 1
    mask = 1 if (y + x) % 2 == 0 else 0
    bitstream.append(str(raw ^ mask))
bitstream = "".join(bitstream)

bom = bitstream[:8]
encrypted = (bom[0] == '0')
key = [int(b) for b in bom[1:]]
rest = [int(b) for b in bitstream[8:]]
if encrypted:
    for i in range(len(rest)):
        rest[i] ^= key[i % 7]

message = []
for i in range(0, len(rest), 7):
    chunk = rest[i:i+7]
    if len(chunk) < 7:
        break
    val = int("".join(str(b) for b in chunk), 2)
    if val == 0:  # EOM
        break
    message.append(chr(val))

print("".join(message))
