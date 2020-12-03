with open("input.txt") as f:
    tree_lines = f.read().splitlines()


def slide_em_bois(tree_lines, right, down):
    position = 0
    tree_count = 0
    bounds = len(tree_lines[0])
    i = 0
    while i <= len(tree_lines) - 1:
        if position >= bounds:
            position -= bounds
        if tree_lines[i][position] == "#":
            tree_count += 1
        position += right
        i += 1 + (down - 1)

    return tree_count


print(slide_em_bois(tree_lines, 3, 1))
