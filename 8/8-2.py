import copy

with open("input.txt") as f:
    instructions = f.read().split("\n")

instructions = [(index, i.split(" ")) for index, i in enumerate(instructions)]
patches = [index for index, ops in instructions if ops[0] in ["nop", "jmp"]]
instructions_original = copy.deepcopy(instructions)


def patch_instruction(index, instructions):
    if instructions[index][1][0] == "jmp":
        instructions[index][1][0] = "nop"
    elif instructions[index][1][0] == "nop":
        instructions[index][1][0] = "jmp"
    return instructions


for patch in patches:
    instructions = patch_instruction(patch, copy.deepcopy(instructions_original))
    visited = set()
    accumulator = 0
    index = 0

    while index < len(instructions):
        this_instruction = instructions[index][1][0]

        if instructions[index][0] in visited:
            break

        visited.add(instructions[index][0])

        if this_instruction == "acc":
            accumulator += int(instructions[index][1][1])

        if this_instruction == "jmp":
            index = index + int(instructions[index][1][1])

        if not (this_instruction == "jmp"):
            index += 1

        if index == len(instructions) - 1:
            print(accumulator)
            break
