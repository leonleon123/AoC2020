def find_encryption_key(a, b):
    i, val, enc = 0, 1, 1
    while val != a:
        i += 1
        val = val * 7 % 20201227
        enc = enc * b % 20201227
    return enc

with open("input.txt") as file:
    print(find_encryption_key(*[int(x) for x in file.read().split("\n")]), sep="\n")
