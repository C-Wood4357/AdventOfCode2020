import collections

with open("input.txt") as f:
    moves = f.read().split("\n")

moves = list(map(lambda x: (x[0], int(x[1:])), moves))
rotates = collections.deque("ESWN")
current = (0, 0)


def move(current, direction, amount):
    if direction == "E":
        current = (current[0] + amount, current[1])
    if direction == "W":
        current = (current[0] - amount, current[1])
    if direction == "N":
        current = (current[0], current[1] + amount)
    if direction == "S":
        current = (current[0], current[1] - amount)
    return current


def rotate_facing(rotates, amount, direction):
    turns = amount // 90
    if direction == "R":
        turns = turns * -1
    rotates.rotate(turns)
    return rotates


for i in moves:
    if i[0] == "F":
        current = move(current, rotates[0], i[1])
    if i[0] in ["L", "R"]:
        rotates = rotate_facing(rotates, i[1], i[0])
    elif i[0] in ["E", "S", "W", "N"]:
        current = move(current, i[0], i[1])

print(abs(current[0]) + abs(current[1]))
