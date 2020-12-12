with open("input.txt") as f:
    rows = f.read().split("\n")

height, width = len(rows), len(rows[0])
changes = [(0, 0)]


def get_seat(h_ind, w_ind):
    if h_ind < 0 or h_ind > height - 1 or w_ind < 0 or w_ind > width - 1:
        return "L"
    return rows[h_ind][w_ind]


def count_adjacent(h_ind, w_ind):
    u, d, r, l = (
        get_seat(h_ind + 1, w_ind),
        get_seat(h_ind - 1, w_ind),
        get_seat(h_ind, w_ind + 1),
        get_seat(h_ind, w_ind - 1),
    )
    ur, ul, dr, dl = (
        get_seat(h_ind + 1, w_ind + 1),
        get_seat(h_ind + 1, w_ind - 1),
        get_seat(h_ind - 1, w_ind + 1),
        get_seat(h_ind - 1, w_ind - 1),
    )
    return [u, d, r, l, ur, ul, dr, dl].count("#")


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
                if count_adjacent(i, j) >= 4:
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
