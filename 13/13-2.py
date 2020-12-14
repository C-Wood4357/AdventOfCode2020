from os import X_OK
from functools import reduce


with open("input.txt") as f:
    notes = f.read().split("\n")

buses = [i for i in notes[1].split(",")]

mods = []
ns = []
for index, bus in enumerate(buses):
    if bus == "x":
        continue
    mods.append(int(bus))
    ns.append(-index % int(bus))

this_x = 0

total = mods[0]
for ind in range(len(mods) - 1):
    while True:
        if this_x % mods[ind + 1] == ns[ind + 1]:
            print("I just solved:", mods[ind + 1])
            total *= mods[ind + 1]
            break
        this_x += total
print(this_x)

# [7,13,x,x,59,x,31,19]

# x = 0 mod 7
# x+1 = 0 mod 13
# x+4 = 0 mod 59
# x+6 = 0 mod 31
# x+7 = 0 mod 19

# 7 * 13 * 69 * 31 * 19 = 3698331

# x = 55 mod 59
# x = 25 mod 31
# x = 12 mod 19
# x = 12 mod 13
# x = 0 mod 7
