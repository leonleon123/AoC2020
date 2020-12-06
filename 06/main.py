from functools import reduce

with open("input.txt") as file:
    t = file.read().split("\n\n")
    print(sum(len(set(b.replace("\n", ""))) for b in t))
    print(sum(len(reduce(lambda a, acc: a.intersection(acc),  map(set, b.split("\n")))) for b in t))
