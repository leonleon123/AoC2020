def valid_pos(field, i, j):
    return i  >= 0 and i  < len(field) and j  >= 0 and j < len(field[0])

def valid(field, i, j, di, dj):
    return valid_pos(field, i+di, j+dj) and (di != 0 or dj != 0)

def next_val_part_1(field, i, j):
    if field[i][j] == ".": return "."
    n = [[field[i + di][j + dj] for dj in range(-1,2) if valid(field, i, j, di, dj)] for di in range(-1,2)]
    s = "".join("".join(filter(lambda e: e != ".", x)) for x in n)
    return ("#" if s.count("#") == 0 else "L") if field[i][j] == "L" else ("L" if s.count("#") >= 4 else "#")

def next_val_part_2(field, i, j):
    if field[i][j] == ".": return "."
    slopes, s = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)], ""
    for di, dj in slopes:
        ii, jj = i, j
        while valid(field, ii, jj, di, dj):
            ii, jj = ii + di, jj + dj
            if field[ii][jj] != ".":
                s += field[ii][jj]
                break
    return ("#" if s.count("#") == 0 else "L") if field[i][j] == "L" else ("L" if s.count("#") >= 5 else "#")

def iteration(field, next_val):
    return ["".join([next_val(field, i, j) for j in range(len(field[0]))]) for i in range(len(field))]

def run(field, next_val):
    new = iteration(field, next_val)
    while new != field:
        field = new
        new = iteration(new, next_val)
        print(*[x for x in new],"", sep="\n")
    return sum(x.count("#") for x in new)

with open("input.txt") as file:
    field = [line.replace("\n", "") for line in file.read().split("\n")]
    p1, p2 = run(field, next_val_part_1), run(field, next_val_part_2)
    print(p1, p2, sep="\n")
