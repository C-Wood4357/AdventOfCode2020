with open("input.txt") as f:
    numbers = f.read().split("\n")


numbers = sorted(list(map(lambda x: int(x), numbers)))
numbers.insert(0, 0)
numbers.append(numbers[-1] + 3)
print(numbers)

three_diffs = 0
one_diffs = 0

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] == 3:
        three_diffs += 1
    if numbers[i + 1] - numbers[i] == 1:
        one_diffs += 1

print("Solution:", three_diffs * one_diffs)
