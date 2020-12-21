from functools import reduce

with open("input.txt") as file:
    data = [(x.split(" (contains ")[0].split(" "), x.split(" (contains ")[1][:-1].split(", ")) for x in file.read().split("\n")]
    alergens, out = {x:[] for x in reduce(lambda a,b: [*a, *b], [a for i, a in data])}, {}
    for i, a in data:
        for alergen in a:
            alergens[alergen].append(set(i))
    for alergen in alergens:
        for a in alergens:
            overlapping = reduce(lambda a,b: a & b, alergens[a])
            if len(overlapping) == 1:
                ingredient = overlapping.pop()
                out[ingredient] = a
                for a in alergens:
                    for i in range(len(alergens[a])):
                        alergens[a][i] = {x for x in alergens[a][i] if x != ingredient}
                break
    print(len([x for x in reduce(lambda a,b: a + b, [i for i,a in data]) if x not in out]))
    print(",".join([i for i,a in sorted(zip(out, out.values()), key=lambda x: x[1])]))
