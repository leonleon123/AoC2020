def p1(a):
    while len(a) > 1:
        a = [str(eval(a.pop(0)+a.pop(0)+a.pop(0))), *a]
    return a[0]

def p2(a):
    while "+" in a:
        i = a.index("+")
        a[i-1:i+2] = [str(eval("".join(a[i-1:i+2])))]
    return p1(a)

def parse(a, calc):
    if a.count("(") == 0 and a.count(")") == 0: return int(calc([*a]))
    else:
        while "(" in a:
            i, prev = 0,0 
            while "(" in a[i:] and (low := a.index("(", i)) < (high := a.index(")", i)):
                i, prev = i+1, low
            a[prev:high+1] = [calc(a[prev+1:high])]
        return int(calc([*a]))

with open("input.txt") as file:
    data = [x.replace("(", "( ").replace(")", " )") for x in file.read().split("\n")]
    print(*[sum(parse(x.split(" "), p) for x in data) for p in [p1,p2]], sep="\n")
