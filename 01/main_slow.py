from math import prod


def sum_to(a, acc, n, to):
    if n == 0: return print(prod(acc)) if sum(acc) == to and acc == sorted(acc) else None
    for i in a: sum_to(a, [*acc, i], n - 1, to)
    
with open("input.txt") as file:
    lines = list(map(int, file.readlines()))
    [sum_to(lines, [], i, 2020) for i in [2,3]]
