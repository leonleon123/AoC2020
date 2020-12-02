def format_tuple(line):
    line_split = line.replace('\n', '').split(' ')
    low, high = [*map(int,line_split[0].split('-'))]
    return low, high, line_split[1][0], line_split[2]

with open("input.txt") as file:
    line_tuples = list(map(format_tuple, file.readlines()))
    print(sum(p.count(c) >= low and p.count(c) <= high for low, high, c, p in line_tuples))
    print(sum((p[low-1] == c or p[high-1] == c) and p[low-1] != p[high-1] for low, high, c, p in line_tuples))
