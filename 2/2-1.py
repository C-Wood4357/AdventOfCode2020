with open("input.txt") as f:
    pass_and_policy = f.read().splitlines()

pandp = list(map(lambda x: x.split(": "), pass_and_policy))

valid_count = 0

for policy, password in pandp:
    minmaxs, letter = policy.split(" ")
    letter_min, letter_max = map(int, minmaxs.split("-"))
    count = sum(map(lambda x: 1 if letter in x else 0, password))
    if letter_min <= count <= letter_max:
        valid_count += 1

print(valid_count)