# https://www.codingame.com/training/easy/equivalent-resistance-circuit-building

def ser(a):
    return round(float(sum(a)), 1)

def par(a):
    return round(float(1/sum(1/x for x in a)), 1)

n = int(input())
val = {}
for ele in range(n):
    inp = input().split()
    val[inp[0]] = int(inp[1])
cir = input().split()

stk = []
for ele in cir:
    if ele in val:
        stk.append(val[ele])
    elif ele == '(':
        stk.append("SER")
    elif ele == '[':
        stk.append("PAR")
    elif ele in [')', ']']:
        temp = []
        while True:
            x = stk.pop()
            if x == "SER" and ele == ")":
                stk.append(ser(temp))
                break
            elif x == "PAR" and ele == "]":
                stk.append(par(temp))
                break
            else:
                temp.append(x)
print(stk[0])
