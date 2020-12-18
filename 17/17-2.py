import numpy as np

with open("input.txt") as f:
    slice = f.read().split("\n")

grid = np.array([list(i.replace(".", "0").replace("#", "1")) for i in slice])

actives = []
for x, i in enumerate(grid):
    for y, j in enumerate(i):
        if j == "1":
            actives.append((x, y, 0, 0))


active = set(actives)

print(actives)
print("----------------------------")


def get_neighbours(x):
    return [
        (i, j, k, l)
        for i in (x[0] - 1, x[0], x[0] + 1)
        for j in (x[1] - 1, x[1], x[1] + 1)
        for k in (x[2] - 1, x[2], x[2] + 1)
        for l in (x[3] - 1, x[3], x[3] + 1)
        if not (i == x[0]) or not (j == x[1]) or not (k == x[2]) or not (l == x[3])
    ]


for l in range(0, 6):
    new_set = set()
    for i in active:
        if len(active.intersection(set(get_neighbours(i)))) in [2, 3]:
            new_set.add(i)
        for neighbour in get_neighbours(i):
            if len(active.intersection(set(get_neighbours(neighbour)))) == 3:
                new_set.add(neighbour)
    active = new_set

print(len(active))