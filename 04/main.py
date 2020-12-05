import re

with open("input.txt") as file:
    data = [{el.split(":")[0]: el.split(":")[1] for el in re.split("\n| ", block)} for block in file.read().split("\n\n")]
    required = {
        "byr": lambda a: a.isdigit() and int(a) >= 1920 and int(a) <= 2002, 
        "iyr": lambda a: a.isdigit() and int(a) >= 2010 and int(a) <= 2020, 
        "eyr": lambda a: a.isdigit() and int(a) >= 2020 and int(a) <= 2030, 
        "hgt": lambda a: re.match("[0-9]*(cm|in)", a) and int(a[:-2]) >= (150 if a[-2:] == "cm" else 59) and int(a[:-2]) <= (193 if a[-2:] == "cm" else 76), 
        "hcl": lambda a: a[0] == "#" and len(re.match("([0-9]|[a-f])*", a[1:]).group()) == 6, 
        "ecl": lambda a: a in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], 
        "pid": lambda a: len(re.match("[0-9]*", a).group()) == 9
    }
    print(sum(all(r in el for r in required) for el in data))
    print(sum(all(r in el for r in required) and all(e not in required or required[e](el[e]) for e in el) for el in data))

