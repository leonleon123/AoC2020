def valid(field, i, j, k, l):
    return all(x >= 0 and x < len(field) for x in [i,j,k,l])

def empty_field(n):
    return [[[[0 for w in range(n)] for z in range(n)] for y in range(n)] for x in range(n)]

def neighbours(field, i, j, k, l):
    out = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            for dk in [-1, 0, 1]:
                for dl in [-1, 0, 1]:
                    if valid(field, i+di, j+dj, k+dk, l+dl) and not (di == 0 and dj == 0 and dk == 0 and dl == 0):
                        out.append(field[i+di][j+dj][k+dk][l+dl])
    return out

def iteration(field):
    n = len(field)
    new_field = empty_field(len(field))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    active_neigbours = sum(neighbours(field, i, j, k, l))
                    if field[i][j][k][l] == 1:
                        new_field[i][j][k][l] = 1*(active_neigbours == 2 or active_neigbours == 3)
                    elif field[i][j][k][l] == 0 and active_neigbours == 3:
                        new_field[i][j][k][l] = 1
    return new_field

with open("input.txt") as file:
    data = file.read().split("\n")
    n = 20
    field = empty_field(n)
    i0 = j0 = n // 2 - len(data) // 2
    for i in range(len(data)):
        for j in range(len(data)):
            field[i+i0][j+j0][n // 2][n // 2] = 1 if data[i][j] == "#" else 0

    for it in range(6):
        field = iteration(field)
    alive = sum(sum(sum(sum(z) for z in y) for y in x) for x in field)
    print(alive)

# this solution is really slow, but today i didn't have time to optimise it :P
