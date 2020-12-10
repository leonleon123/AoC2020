from math import prod

diff = lambda d: [d[i+1]-d[i] for i in range(len(d)-1)]

with open("input.txt") as file:
    d = sorted(map(int, file.readlines()))
    df = [1] + diff(d) + [3]
    rle = diff([-1] + [i for i, x in enumerate(diff(df)) if x != 0] + [len(df)-1])
    m = [2**x - sum("000" in bin(y)[2:].zfill(x) for y in range(2**x)) for x in range(max(rle) + 1)]
    print(df.count(1)*df.count(3))
    print(prod(m[x-1] for i, x in enumerate(rle) if i % 2 == 0))
