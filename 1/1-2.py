with open("input.txt") as f:
    nums = f.read().splitlines()

nums = sorted(list(map(int, nums)), reverse=True)

print(nums)

target = 2020

for i in nums:
    search_value = target - i
    print(f"Search: {search_value}, i: {i}")
    out = list(filter(lambda x: x <= search_value, reversed(nums)))
    for j in out:
        second_search_value = search_value - j
        if j <= 0:
            continue
        out2 = list(filter(lambda x: x <= second_search_value, reversed(out)))
        if second_search_value in out:
            print("FOUND VALUE:", i * j * second_search_value)
            exit()
