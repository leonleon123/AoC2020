from functools import reduce


def find_colors(m, key):
    return reduce(lambda x,y: x|y, [set(m[key])] + [find_colors(m, c) for c in m[key]]) if key in m else set()

def find_required(m, key):
    return sum(count + count * find_required(m, c) for count, c in m[key]) if key in m else 0

with open("input.txt") as file:
    a, b = {}, {}
    for line in file.readlines():
        color, contains = line.split(" bags contain ")
        if not "no other bags" in contains:
            for count, c in [(c.split(" ")[0], " ".join(c.split(" ")[1:3])) for c in contains.split(", ")]:
                a[c], b[color] = [*(a[c] if c in a else []), color], [*(b[color] if color in b else []), (int(count), c)]
    print(len(find_colors(a, "shiny gold")), find_required(b, "shiny gold"), sep="\n")
