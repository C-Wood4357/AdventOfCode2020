with open("input.txt") as f:
    numbers = f.read().split(",")

numbers = [int(n) for n in numbers]


def get_num_spoken(max_index):
    num_dict = {}
    index = 0
    for ind, num in enumerate(numbers[:-1]):
        num_dict[num] = ind + 1
        index += 1

    lnum = numbers[-1]
    index = len(numbers) + 1

    while index <= max_index:
        if lnum not in num_dict.keys():
            nextn = 0
            num_dict[lnum] = index - 1

        else:
            nextn = index - num_dict[lnum] - 1
            num_dict[lnum] = index - 1

        lnum = nextn
        index += 1

    print("Final:", nextn)
    return lnum


print(get_num_spoken(30000000))