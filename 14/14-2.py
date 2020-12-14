import re
from itertools import product, chain
import numpy as np

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


def first_pass(mask, bits):
    new_value = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            new_value += bits[i]
        else:
            new_value += mask[i]
    return new_value


def handle_floating(curr_mask, p_bits, index):

    if index >= len(p_bits):
        return p_bits
    if curr_mask[index] == "X":
        floatz = p_bits[:index] + "1" + p_bits[index + 1 :]
        floato = p_bits[:index] + "0" + p_bits[index + 1 :]
        return [handle_floating(curr_mask, floatz, index + 1)] + [
            handle_floating(curr_mask, floato, index + 1)
        ]

    else:
        return handle_floating(curr_mask, p_bits, index + 1)


for op, value in values:
    if op == "mask":
        curr_mask = value
    elif op.startswith("mem"):
        address = re.search(mem_addr, op)[1]
        address_bits = (format(int(address), "b")).rjust(36, "0")
        address_bits = first_pass(curr_mask, address_bits)
        address_list = handle_floating(curr_mask, address_bits, 0)
        address_list = np.array(address_list).flatten()
        address_list = list(map(lambda x: int(x, 2), address_list))
        for i in address_list:
            memory[i] = int(value)

# print(memory)

print(sum(memory.values()))