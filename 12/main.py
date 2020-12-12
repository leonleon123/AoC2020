def no_waypoint(data, m, p, d):
    for ac, val in data:
        d = (d + int(val / 90)*(1 - 2 * (ac == "L"))) % 4 if ac in "LR" else d
        t = ac if ac in m else list(m.keys())[d]
        p = (p[0] + m[t][0] * val, p[1] + m[t][1] * val) if not ac in "LR" else p
    return sum(abs(x) for x in p)

def waypoint(data,m, p, w):
    for ac, val in data:
        [w := (w[1]*(1-2*(ac=="L")), w[0]*(1-2*(ac=="R"))) for i in range(int(val/90))] if ac in "LR" else []
        w = (w[0] + m[ac][0] * val, w[1] + m[ac][1] * val) if ac in m else w
        p = (p[0] + w[0] * val, p[1] + w[1] * val) if ac == "F" else p
    return sum(abs(x) for x in p)

with open("input.txt") as file:
    data = [(line[0], int(line[1:])) for line in file.readlines()]
    m = {"S": (1, 0), "W": (0, -1),"N": (-1, 0), "E": (0, 1)}
    print(no_waypoint(data, m, (0,0), 3), waypoint(data, m, (0,0), (-1, 10)), sep="\n")
