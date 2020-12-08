with open("input.txt") as f:
    instructions = f.read().split("\n")

visited = set()
instructions = [(index, i.split(" ")) for index, i in enumerate(instructions)]
accumulator = 0
index = 0

while index < len(instructions):
    if instructions[index][0] in visited:
        break

    visited.add(instructions[index][0])

    if instructions[index][1][0] == "acc":
        accumulator += int(instructions[index][1][1])

    elif instructions[index][1][0] == "jmp":
        index = index + int(instructions[index][1][1])
        continue

    index += 1

print(accumulator)