with open("input.txt") as f:
    nums = f.read().splitlines()

nums = sorted(list(map(int, nums)), reverse=True)

print(nums)

target = 2020

for i in nums:
    search_value = target - i
    print(f"Search: {search_value}, i: {i}")
    out = list(filter(lambda x: x <= search_value, reversed(nums)))
    if search_value in out:
        print("FOUND VALUE:", i * search_value)
        exit()
