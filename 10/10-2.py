from functools import reduce

with open("input.txt") as f:
    numbers = f.read().split("\n")

n = sorted(list(map(lambda x: int(x), numbers)))
n.insert(0, 0)
n.append(n[-1] + 3)

target = n[-1]

memoize = {}


def part2(number):
    if number == target:
        return 1
    if number in memoize.keys():
        return memoize[number]
    paths = 0
    if number + 1 in n:
        paths += part2(number + 1)
    if number + 2 in n:
        paths += part2(number + 2)
    if number + 3 in n:
        paths += part2(number + 3)
    memoize[number] = paths
    print(number, paths)
    return paths


print("Total:", part2(0))
