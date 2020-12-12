with open("input.txt") as f:
    rows = f.read().split("\n")

height, width = len(rows), len(rows[0])
changes = [(0, 0)]

direction = {
    "u": [1, 0],
    "d": [-1, 0],
    "r": [0, 1],
    "l": [0, -1],
    "ur": [1, 1],
    "ul": [1, -1],
    "dr": [-1, 1],
    "dl": [-1, -1],
}


def get_seat(h_ind, w_ind):
    if h_ind < 0 or h_ind > height - 1 or w_ind < 0 or w_ind > width - 1:
        return "L"
    return rows[h_ind][w_ind]


def iterate_get_seat(h_ind, w_ind, dir):
    if get_seat(h_ind + direction[dir][0], w_ind + direction[dir][1]) == ".":
        return iterate_get_seat(
            h_ind + direction[dir][0], w_ind + direction[dir][1], dir
        )
    if get_seat(h_ind + direction[dir][0], w_ind + direction[dir][1]) == "L":
        return "L"
    else:
        return "#"


def count_adjacent(h_ind, w_ind):
    first_seat_count = []
    for i in ["u", "d", "r", "l", "ur", "ul", "dr", "dl"]:
        first_seat_count.append(iterate_get_seat(h_ind, w_ind, i))
    return first_seat_count.count("#")


while len(changes) > 0:
    changes = []
    nextrows = [["." for x in range(width)] for y in range(height)]
    for i in range(height):
        for j in range(width):
            if rows[i][j].__eq__("L"):
                if count_adjacent(i, j) == 0:
                    nextrows[i][j] = "#"
                    changes.append((i, j))
                else:
                    nextrows[i][j] = "L"
            elif rows[i][j].__eq__("#"):
                if count_adjacent(i, j) >= 5:
                    nextrows[i][j] = "L"
                    changes.append((i, j))
                else:
                    nextrows[i][j] = "#"
            else:
                nextrows[i][j] = rows[i][j]
    rows = nextrows

seat_count = 0
for i in rows:
    for j in i:
        if j == "#":
            seat_count += 1
print(seat_count)
