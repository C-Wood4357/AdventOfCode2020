from itertools import combinations

with open("input.txt") as f:
    numbers = f.read().split("\n")

numbers = list(map(lambda x: int(x), numbers))
window = 25
invalid_num = 0

for i in range(len(numbers)):
    pairs = list(combinations(numbers[i : i + window], 2))
    sums = [pair[0] + pair[1] for pair in pairs if pair[0] != pair[1]]
    fail = True
    if numbers[i + window] in sums:
        fail = False

    if fail:
        invalid_num = numbers[i + window]
        print("Preamble ends at:", invalid_num)
        break
