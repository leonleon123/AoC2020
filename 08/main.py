def run(data):
    pc, acc, ex = 0, 0, set()
    while pc not in ex:
        if pc < 0 or pc >= len(data): return pc, acc
        ex.add(pc)
        op, ar = data[pc]
        acc += (op == "acc") * ar
        pc += (ar - 1) * (op == "jmp") + 1
    return pc, acc
        
with open("input.txt") as file:
    data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file.readlines()]
    print(run(data)[1])
    max_pc, max_acc = 0, 0
    for i in range(len(data)):
        op, ar = data[i]
        if op == "jmp" or op == "nop":
            tmp = [*data]
            tmp[i] = ("jmp" if op == "nop" else "nop", ar)
            pc, acc = run(tmp)
            if pc > max_pc: max_pc, max_acc = pc, acc
    print(max_acc)
