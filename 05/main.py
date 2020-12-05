with open("input.txt") as file:
    r = {"B": "1", "F": "0", "R": "1", "L": "0", "\n":""}
    s = sorted(int("".join(map(lambda c: r[c], line)), 2) for line in file.readlines())
    print(max(s), s[[s[i+1] - s[i] for i in range(len(s)-1)].index(2)] + 1, sep="\n")
