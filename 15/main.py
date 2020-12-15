def nth(spoken, num):
    new, spoken = spoken[-1], {x:i for i,x in enumerate(spoken[:-1])}
    for n in range(len(spoken), num):
        last, new = new, abs(n - spoken[new]) if new in spoken else 0
        spoken[last] = n
    return last

with open("input.txt") as file:
    spoken = list(map(int, file.read().split(",")))
    print(nth(spoken, 2020), nth(spoken, 30000000), sep="\n")
