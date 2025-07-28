# https://www.codingame.com/training/easy/crop-circles

SPC, PLT = "  ", "{}"
WDT, HGT = 19, 25

ipt = input().split()

fld = [[PLT for _ in range(WDT)] for _ in range(HGT)]

for i in ipt:
    if i.startswith("PLANTMOW"):
        act = "PLANTMOW"
    elif i.startswith("PLANT"):
        act = "PLANT"
    else:
        act = "MOW"

    gps = i.replace(act, "")
    gx, gy = gps[0], gps[1]
    cx, cy = ord(gx) - ord("a"), ord(gy) - ord("a")
    d = int(gps[2:])
    r = d / 2

    for y in range(HGT):
        for x in range(WDT):
            dx, dy = x - cx, y - cy
            if dx*dx + dy*dy <= r*r:
                if act == "PLANT":
                    fld[y][x] = PLT
                elif act == "PLANTMOW":
                    fld[y][x] = SPC if fld[y][x] == PLT else PLT
                else:
                    fld[y][x] = SPC

for rw in fld:
    print("".join(rw))
