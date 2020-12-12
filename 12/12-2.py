import collections
import numpy as np

with open("input.txt") as f:
    moves = f.read().split("\n")

moves = list(map(lambda x: (x[0], int(x[1:])), moves))
sc = (0, 0)
wc = (10, 1)


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


def move_to_waypoint(shipc, wayc, amount):
    return (shipc[0] + (wayc[0] * amount), shipc[1] + (wayc[1] * amount))


def rotate_facing(rotates, amount, direction):
    turns = amount // 90
    if direction == "R":
        turns = turns * -1
    rotates.rotate(turns)
    return rotates


def rotate_waypoint(wc, amount, direction):
    theta = np.radians(amount)
    if direction == "R":
        theta = -theta
    rotation_matrix = np.array(
        ((np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta)))
    )
    v = np.array((wc[0], wc[1]))
    return (rotation_matrix.dot(v)[0], rotation_matrix.dot(v)[1])


for i in moves:
    if i[0] == "F":
        sc = move_to_waypoint(sc, wc, i[1])
    if i[0] == "R":
        wc = rotate_waypoint(wc, i[1], i[0])
    if i[0] == "L":
        wc = rotate_waypoint(wc, i[1], i[0])
    elif i[0] in ["E", "S", "W", "N"]:
        wc = move(wc, i[0], i[1])

print(round(abs(sc[0]) + abs(sc[1])))
