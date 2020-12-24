import os

with open("input.txt") as f:
    decks = f.read().split("\n\n")

p1 = decks[0].split("\n")
p2 = decks[1].split("\n")

p1, p2 = [int(i) for i in p1 if "Player" not in i], [
    int(i) for i in p2 if "Player" not in i
]


def play_game(p1, p2):
    while len(p1) >= 0 and len(p2) >= 0:
        if p1 == []:
            return p2
        if p2 == []:
            return p1
        else:
            p1_top, p2_top = p1.pop(0), p2.pop(0)

            if p1_top > p2_top:
                p1.append(p1_top)
                p1.append(p2_top)
            else:
                p2.append(p2_top)
                p2.append(p1_top)


total = 0
for i, val in enumerate(reversed(play_game(p1, p2))):
    total += (i + 1) * val
print(total)