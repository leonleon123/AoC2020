from math import prod

xi = lambda Ni, bi, mod: [(Ni % mod) * i % mod for i in range(mod)].index(1)

with open("input.txt") as file:
    t = int(file.readline())
    d = [(x[0], int(x[1])) for x in enumerate(file.readline().split(",")) if x[1] != "x"]
    c = min(enumerate([i * (t // i + 1) for i in map(lambda x: x[1], d)]), key = lambda x: x[1])
    b_i, mod_i, N = [(x - i) % x for i,x in d], [x for i, x in d], prod(x for i, x in d)
    print(d[c[0]][1]*(c[1]-t))
    print(sum(xi(Ni,bi,mod)*Ni*bi for Ni,bi,mod in zip([N // x for i,x in d],b_i,mod_i)) % N)
