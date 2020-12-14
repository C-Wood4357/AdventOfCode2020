import re

with open("input.txt") as f:
    values = f.read().split("\n")

values = list(
    map(
        (
            lambda x: (
                "".join(x.split("=")[0].rsplit()),
                "".join(x.split("=")[1].rsplit()),
            )
        ),
        values,
    )
)

mem_addr = re.compile(r"\[([^]]+)\]")

curr_mask = ""
memory = {}
for op, value in values:
    if op == "mask":
        curr_mask = value
    elif op.startswith("mem"):
        address = re.search(mem_addr, op)
        bit_value = (format(int(value), "b")).rjust(36, "0")
        new_value = ""
        for i in range(len(curr_mask)):
            if curr_mask[i] == "X":
                new_value += bit_value[i]
            else:
                new_value += curr_mask[i]
        memory[address] = int(new_value, 2)


print(sum(memory.values()))