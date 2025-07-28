# https://www.codingame.com/training/easy/card-counting-when-easily-distracted

dck = {
    "A": {"val": 1, "qty": 4},
    "K": {"val": 10, "qty": 4},
    "Q": {"val": 10, "qty": 4},
    "J": {"val": 10, "qty": 4},
    "T": {"val": 10, "qty": 4},
    **{str(n): {"val": n, "qty": 4} for n in range(2, 10)}
}
clr = ""
lwr, hgr = 0, 0

stm = input().split(".")
bst = int(input())

for chk in stm:
    vld = True
    for ltr in chk:
        if ltr not in dck:
            vld = False
    if vld:
        clr += str(chk)

for crd in clr:
    dck[crd]["qty"] -= 1

for crd in dck:
    if dck[crd]["val"] >= bst:
        hgr += dck[crd]["qty"]
    else:
        lwr += dck[crd]["qty"]

print(f"{round((lwr/(lwr+hgr))*100)}%")
