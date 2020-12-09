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
        break

for i in range(len(numbers)):
    total = numbers[i]
    j = i + 1
    while j <= len(numbers):
        if total == invalid_num and j - i > 1:
            print(numbers[i:j], sum(numbers[i:j]))
            print(
                "Weakness:",
                min(numbers[i:j]) + max(numbers[i:j]),
            )
            break

        if total > invalid_num:
            break
        total = total + numbers[j]
        j += 1