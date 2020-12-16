import re
import numpy as np

with open("input.txt") as f:
    notes = f.read().split("\n\n")

rules = notes[0].split("\n")
my_ticket = notes[1].split("\n")[1:][0].split(",")
near_tickets = notes[2].split("\n")[1:]
near_tickets = [[int(y) for y in t.split(",")] for t in near_tickets]

rules_dict = {}
rule_range = re.compile(r"([\d]*)?-([\d]*)?")


def valid_for_rule(value, rule):
    i = rules_dict[rule]
    if value >= i[0][0] and value <= i[0][1]:
        return True
    elif value >= i[1][0] and value <= i[1][1]:
        return True
    return False


def valid_for_any(value):
    for i in rules_dict.values():
        if value >= i[0][0] and value <= i[0][1]:
            return True
        elif value >= i[1][0] and value <= i[1][1]:
            return True
    return False


def has_invalid(invalid, ticket):
    ticket = i.split(",")
    for value in ticket:
        if int(value) in invalid:
            return True
    return False


for i in rules:
    field = i.split(":")[0]
    for lower, higher in re.findall(rule_range, i):
        if rules_dict.get(field):
            rules_dict[field].append((int(lower), int(higher)))
        else:
            rules_dict[field] = [(int(lower), int(higher))]

invalid = []
invalid_indexes = []

for index, i in enumerate(near_tickets):
    for v in i:
        if not (valid_for_any(int(v))):
            invalid.append(int(v))
            invalid_indexes.append(int(index))

valid_tickets = []

for index, i in enumerate(near_tickets):
    if not (index in invalid_indexes):
        valid_tickets.append(i)

field_dict = {}
ticket_matrix = np.array(valid_tickets)

for j in rules_dict.keys():
    for ind, col in enumerate(ticket_matrix.T):
        if all([valid_for_rule(value, j) for value in col]):
            if field_dict.get(j):
                field_dict[j].append(ind)
            else:
                field_dict[j] = [ind]

fields_sort = sorted(list(field_dict.items()), key=lambda tup: len(tup[1]))

seen = set()
new_dict = {}

for j in fields_sort:
    new_ind = 0
    for ind in j[1]:
        if ind not in seen:
            seen.add(ind)
            new_dict[j[0]] = ind

departure_inds = {
    key: val for key, val in new_dict.items() if key.startswith("departure")
}.values()

total = 1
for i in departure_inds:
    total *= int(my_ticket[i])

print(total)
