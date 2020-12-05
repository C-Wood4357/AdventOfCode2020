with open("input.txt") as f:
    passes = f.read().split("\n")

highest = 0
seats_list = []

for i in passes:
    row_num = int(i[:7].replace("B", "1").replace("F", "0"), 2)
    seat_num = int(i[7:].replace("R", "1").replace("L", "0"), 2)
    number = (row_num * 8) + seat_num
    if number >= highest:
        highest = number
    seats_list.append(number)

for i in range(850):
    if i not in seats_list:
        if i - 1 in seats_list and i + 1 in seats_list:
            print("My Seat: ", i)