def run(data):
    pc, acc, ex = 0, 0, set()
    while pc not in ex:
        if pc < 0 or pc >= len(data): break
        ex.add(pc)
        op, ar = data[pc]
        acc, pc = acc + (op == "acc") * ar, pc +  (ar - 1) * (op == "jmp") + 1
    return pc, acc
        
with open("input.txt") as file:
    d = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file.readlines()]
    print(run(d)[1])
    swapped = [run(d[:i] + [(["jmp", "nop"][d[i][0] == "jmp"], d[i][1])] + d[i+1:]) for i in range(len(d)) if d[i][0] in ["jmp", "nop"]]
    print(max(swapped, key=lambda e: e[0])[1])
