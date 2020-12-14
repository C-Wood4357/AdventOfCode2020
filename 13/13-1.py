with open("input.txt") as f:
    notes = f.read().split("\n")

timestamp = int(notes[0])
start = timestamp
buses = [i for i in notes[1].split(",")]
buses = [bus for bus in buses if bus != "x"]


print(timestamp, buses)

buscheck = False
while timestamp < 999999999 and buscheck == False:
    for i in buses:
        if timestamp % int(i) == 0:
            print(int(i) * (timestamp - start), i, timestamp)
            buscheck = True
            break
    timestamp += 1