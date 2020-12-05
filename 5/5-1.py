with open("input.txt") as f:
    passes = f.read().split("\n")

highest = 0

for i in passes:
    row_num = int(i[:7].replace("B", "1").replace("F", "0"), 2)
    seat_num = int(i[7:].replace("R", "1").replace("L", "0"), 2)
    number = (row_num * 8) + seat_num
    if number >= highest:
        highest = number

print("Highest:", highest)