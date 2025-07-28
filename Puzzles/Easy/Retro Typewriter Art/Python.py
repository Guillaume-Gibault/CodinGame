# https://www.codingame.com/training/easy/retro-typewriter-art

ABBREVIATIONS = {
    "sp": " ",
    "bS": "\\",
    "sQ": "'",
}

i = input().split()
b = ""

for chu in i:
    if chu == "nl":
        print(b)
        continue
    for a in ABBREVIATIONS:
        chu = chu.replace(a, ABBREVIATIONS[a])
    n, cha = int(chu[:len(chu)-1]), chu[-1:]
    print(n*cha, end="")
