import re


def parse_rules(lines):
    return {n: r for n,r in [(line.split(": ")[0], [r.split(" ") for r in line.split(": ")[1].split(" | ")]) for line in lines]}

def regexify(rules, rule):
    return "("+"|".join( "".join(regexify(rules, x) if x.isdigit() else x.replace("\"", "") for x in p) for p in rules[rule]) +")"

def check_repeat(line, r42, r31, r0):
    if re.match(r42, line) and not re.fullmatch(r0, line):
        i, j = 0, 0
        while (m := re.match(r42, line)):
            low, high = m.span()
            line, i = line[high:], i + 1
        if len(line) == 0: return False
        while (m := re.match(r31, line)):
            low, high = m.span()
            line, j = line[high:], j + 1
        return len(line) == 0 and i > j
    else: return False

with open("input.txt") as file:
    rule_block, message_block = file.read().split("\n\n")
    rules = parse_rules([rule for rule in rule_block.split("\n")])
    r0, r42, r31 = regexify(rules, '0'), regexify(rules, '42'), regexify(rules, '31')
    print(count := sum(1 if re.fullmatch(r0, line) else 0 for line in message_block.split("\n"))) 
    print(count + sum(check_repeat(line, r42, r31, r0) for line in message_block.split("\n")))
