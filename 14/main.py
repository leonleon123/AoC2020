def sub_bin(tmp, i, n, c):
    for x in bin(i)[2:].zfill(n):
        tmp[tmp.index(c)] = x
    return "".join(tmp)

def replace_floating(adr, mask):
    n, adr = mask.count("X"), [m if m in "1X" else v for m, v in zip(mask, adr)]
    return [sub_bin([*adr], i, n, "X") for i in range(2**n)]

with open("input.txt") as file:
    p1, p2 = {}, {}
    for line in file.read().split("\n"):
        adr, val = line.split(" = ")
        if adr == "mask":
            mask = val
        else:
            p1[int(adr[4:-1])] = (int(val) | int(mask.replace("X", "0"), 2)) & int(mask.replace("X", "1"), 2)
            for a in replace_floating(bin(int(adr[4:-1]))[2:].zfill(36), mask):
                p2[a] = int(val)
    print(sum(p1.values()), sum(p2.values()), sep="\n")
