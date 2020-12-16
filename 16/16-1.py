import re

with open("input.txt") as f:
    notes = f.read().split("\n\n")


rules = notes[0].split("\n")
my_ticket = notes[1].split("\n")[1:]
near_tickets = notes[2].split("\n")[1:]

rules_dict = {}
rule_range = re.compile(r"([\d]*)?-([\d]*)?")


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
    values = i.split(",")
    for v in values:
        if not (valid_for_any(int(v))):
            invalid.append(int(v))
            invalid_indexes.append(int(index))

# print(invalid)
print(sum(invalid))
# print(invalid_indexes)

# count = 0
# for i in near_tickets:
#     if has_invalid(invalid, i):
#         count += 1

# print("invalid count:", count)


# values = list(
#     map(
#         (
#             lambda x: (
#                 "".join(x.split("=")[0].rsplit()),
#                 "".join(x.split("=")[1].rsplit()),
#             )
#         ),
#         values,
#     )
# )
