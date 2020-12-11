def valid(field, i, j, di, dj):
    return i + di  >= 0 and i + di < len(field) and j + dj  >= 0 and j + dj < len(field[0]) and (di != 0 or dj != 0)

def next_val_1(field, i, j):
    if field[i][j] == ".": return "."
    c = sum(field[i + di][j + dj] == "#" for dj in range(-1,2) for di in range(-1,2) if valid(field, i, j, di, dj))
    return ("#" if c == 0 else "L") if field[i][j] == "L" else ("L" if c >= 4 else "#")

def next_val_2(field, i, j):
    if field[i][j] == ".": return "."
    slopes, c = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)], 0
    for di, dj in slopes:
        ii, jj = i, j
        while valid(field, ii, jj, di, dj):
            ii, jj = ii + di, jj + dj
            if field[ii][jj] != ".":
                c += 1 if field[ii][jj] == "#" else 0
                break
    return ("#" if c == 0 else "L") if field[i][j] == "L" else ("L" if c >= 5 else "#")

def iteration(field, next_val):
    return ["".join([next_val(field, i, j) for j in range(len(field[0]))]) for i in range(len(field))]

def run(field, next_val):
    new = iteration(field, next_val)
    while new != field:
        field, new = new, iteration(new, next_val)
        print(*new,"", sep="\n")
    return sum(x.count("#") for x in new)

with open("input.txt") as file:
    field = [line.replace("\n", "") for line in file.read().split("\n")]
    print(run(field, next_val_1), run(field, next_val_2), sep="\n")
