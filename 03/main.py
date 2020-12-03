from math import prod


def trees(data, right, down):
    return sum(data[i][j] == "#" for i,j in [(i, int(i*right/down) % len(data[0])) for i in range(down, len(data), down)])

with open("input.txt") as file:
    data = [line.replace("\n", "") for line in file.readlines()]
    print(trees(data, 3, 1), prod(trees(data, right, down) for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]), sep="\n")
