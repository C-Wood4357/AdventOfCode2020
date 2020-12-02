with open("input.txt") as f:
    pass_and_policy = f.read().splitlines()

pandp = list(map(lambda x: x.split(": "), pass_and_policy))

valid_count = 0

for policy, password in pandp:
    indices, letter = policy.split(" ")
    first_ind, second_ind = map(int, indices.split("-"))

    if (password[first_ind - 1] == letter) ^ (password[second_ind - 1] == letter):
        valid_count += 1

print(valid_count)