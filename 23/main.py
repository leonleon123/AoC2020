from math import prod


def init_indices(cups, add = 0):
    n = len(cups)
    indices = [cups[(cups.index(i + 1) + 1) % n] for i in range(n)]
    if add > 0:
        tmp = indices[cups[-1] - 1]
        indices[cups[-1] - 1] = max(cups) + 1
        indices += list(range(max(cups) + 2, add + 1)) + [tmp]
    return indices

def get_n_next(start, indices, n):
    return [indices[start - 1]] + get_n_next(indices[start - 1], indices, n - 1) if n > 0 else []

def compute(cups, iterations, n_next, add = 0):
    indices = init_indices(cups, add)
    curr, n = cups[0], len(indices)
    for i in range(iterations):
        [x, y, z, c] = get_n_next(curr, indices, 4)
        dest = curr - 2 if curr - 2 >= 0 else n-1
        while dest + 1 in [x,y,z]:
            dest = (dest - 1) % n
        indices[z - 1] = indices[dest]
        indices[dest] = x
        indices[curr - 1] = c
        curr = c
    return get_n_next(1, indices, n_next)

with open("input.txt") as file:
    cups = [int(x) for x in file.read()]
    print("".join(str(x) for x in compute(cups, 100, len(cups)-1)))
    print(prod(compute(cups, 10000000, 2, 1000000)))
    