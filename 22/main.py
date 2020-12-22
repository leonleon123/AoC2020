def recursive_combat(p1, p2):
    prev_rounds = []
    while len(p1) > 0 and len(p2) > 0 and (p1, p2) not in prev_rounds:
        prev_rounds.append(([*p1],[*p2]))
        c1, c2 = p1.pop(0), p2.pop(0)
        winner = recursive_combat(p1[:c1], p2[:c2])[1] if len(p1) >= c1 and len(p2) >= c2 else c1 > c2 
        p1, p2 = p1 + ([c1, c2] if winner else []), p2 + ([c2, c1] if not winner else [])
    cond = len(p1) > 0 or (p1,p2) in prev_rounds
    return (p1 if cond else p2, cond)

def combat(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        c1, c2 = p1.pop(0), p2.pop(0)
        p1, p2 = p1 + ([c1, c2] if c1 > c2 else []), p2 + ([c2, c1] if c2 > c1 else [])
    return (p1 if len(p1) > 0 else p2, None)

with open("input.txt") as file:
    p1, p2 = [[int(x) for x in block.split("\n")[1:] if x] for block in file.read().split("\n\n")]
    p = combat([*p1], [*p2]), recursive_combat([*p1], [*p2])
    print(*[sum([x*y for x,y in zip(range(len(x[0]), 0, -1), x[0])]) for x in p], sep="\n")
