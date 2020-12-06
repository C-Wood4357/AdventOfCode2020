with open("input.txt") as f:
    groups = f.read().split("\n\n")

groups = list(map(lambda x: len(set("".join(x.split("\n")))), groups))

print(sum(groups))