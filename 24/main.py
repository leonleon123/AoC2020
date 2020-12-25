import re


def neighbours(field, dir_map, pos):
    return [field[pos[0] + di][pos[1] + dj] for di, dj in [dir_map[e][len(field[pos[0]]) % 2] for e in dir_map]]

def iteration(n, field, dir_map):
    field_tmp = [x[:] for x in field]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            c = sum(neighbours(field, dir_map, (i, j)))
            if field[i][j] == 1 and c == 0 or c > 2: field_tmp[i][j] = 0
            elif field[i][j] == 0 and c == 2: field_tmp[i][j] = 1
    return field_tmp

def print_field(field):
    print(*[(" " if len(x) % 2 == 0 else "") + " ".join(str(y) for y in x) for x in field], sep="\n")

with open("input.txt") as file:
    dir_map = {
        "e":    [( 0,  1),  ( 0,  1)], 
        "se":   [( 1,  1),  ( 1,  0)], 
        "sw":   [( 1,  0),  ( 1, -1)],
        "w":    [( 0, -1),  ( 0, -1)], 
        "nw":   [(-1,  0),  (-1, -1)],
        "ne":   [(-1,  1),  (-1,  0)]    
    }
    paths = [re.findall("|".join(dir_map), x) for x in file.read().split("\n")]
    n = max(len(x) for x in paths) * 10
    field = [[0] * (n + i % 2) for i in range(n)]
    for path in paths:
        pos = [n//2, n//2]
        for m in path:
            di, dj = dir_map[m][len(field[pos[0]]) % 2]
            pos[0] += di
            pos[1] += dj
        field[pos[0]][pos[1]] = (field[pos[0]][pos[1]] + 1) % 2
    print(sum(sum(x) for x in field))
    for i in range(100):
        field = iteration(n, field, dir_map)
    print(sum(sum(x) for x in field))
    