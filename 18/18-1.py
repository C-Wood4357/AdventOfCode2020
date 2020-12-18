from functools import partial


class Infix(object):
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)


@Infix
def add(x, y):
    return x + y


@Infix
def mul(x, y):
    return x * y


with open("input.txt") as f:
    slice = f.read().split("\n")

slice = [
    i.replace(" ", "").replace("*", "| mul |").replace("+", "| add |") for i in slice
]

total = 0
for i in slice:
    # God bless Eval
    total += eval(i)

print(total)