def valid(field, i, j, k):
    return i >= 0 and i < len(field) and j >= 0 and j < len(field) and k >= 0 and k < len(field)

def neighbours(field, i, j, k):
    out = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            for dk in [-1, 0, 1]:
                if valid(field, i+di, j+dj, k+dk) and not (di == 0 and dj == 0 and dk == 0):
                    out.append(field[i+di][j+dj][k+dk])
    return out

def iteration(field):
    w = len(field)
    new_field = [[[0 for z in range(w)] for y in range(w)] for x in range(w)]
    for i in range(w):
        for j in range(w):
            for k in range(w):
                n = sum(neighbours(field, i, j, k))
                if field[i][j][k] == 1:
                    new_field[i][j][k] = 1*(n == 2 or n == 3)
                elif field[i][j][k] == 0 and n == 3:
                    new_field[i][j][k] = 1
    return new_field

with open("input.txt") as file:
    data = file.read().split("\n")
    w = 20
    field = [[[0 for z in range(w)] for y in range(w)] for x in range(w)]
    i0 = j0 = w // 2 - len(data) // 2
    for i in range(len(data)):
        for j in range(len(data)):
            field[i+i0][j+j0][w // 2] = 1 if data[i][j] == "#" else 0 

    for it in range(6):
        field = iteration(field)
    alive = sum(sum(sum(y) for y in x) for x in field)
    print(alive)
