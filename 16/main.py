from math import prod


def parse_rule(line: str):
    name, val = line.split(": ")
    return [tuple(map(int, x.split("-"))) for x in val.split(" or ")]

def part1(rules, ticket):
    return sum(el for el in ticket if not any(any(el >= low and el <= high for low, high in rule) for rule in rules))

def valid(rules, ticket):
    return not any(not any(any(el >= low and el <= high for low, high in rule) for rule in rules) for el in ticket)

def check_rule(rule, arr):
    return all(any(el >= low and el <= high for low, high in rule) for el in arr)

with open("input.txt") as file:
    rules, your, nearby = [block.split("\n") for block in file.read().split("\n\n")]
    rule_names = [rule.split(": ")[0] for rule in rules]
    rules, your = list(map(parse_rule, rules)), list(map(int, your[1].split(",")))
    nearby = [list(map(int, x.split(","))) for x in nearby[1:]]
    print(sum(part1(rules, ticket) for ticket in nearby))
    nearby = [ticket for ticket in nearby if valid(rules, ticket)]
    sat = [[check_rule(rule, [t[i] for t in nearby]) for i in range(len(rules))] for rule in rules]
    sat_T = [[sat[j][i] for j in range(len(sat))] for i in range(len(sat[0]))]
    ind = [-1]*len(sat)
    for row, el in sorted(enumerate([sum(x)-1 for x in sat_T]), key=lambda x: x[1]):
        ind[row] = [i for i, e in enumerate(sat_T[row]) if i not in ind and e][0]
    departure_ind = [i for i, name in enumerate(rule_names) if name.startswith("departure")]
    rule_order = [x for i, x in enumerate([ind.index(i) for i in range(len(sat))]) if i in departure_ind]
    print(prod([your[i] for i in rule_order]), sep="\n")
