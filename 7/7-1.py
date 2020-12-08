import re

with open("input.txt") as f:
    bag_list = f.read().split("\n")

identify_bag = re.compile(r"([0-9]?) *([a-z]*)? ([a-z]*)? bag[s]?")
bag_dict = {}

# Interesting bug here, can you see why I was ending up with 'No Key' errors for bags containing no other bags?
for j in bag_list:
    key_bag = ""
    child_bags = []
    for i in re.findall(identify_bag, j):
        if i[0] == "":
            key_bag = i[1] + "-" + i[2]
        else:
            child_bags.append((i[1] + "-" + i[2], i[0]))
    children, counts = [
        [bag for bag, count in child_bags],
        [count for bag, count in child_bags],
    ]
    bag_dict[key_bag] = children


def gold_mine(bag):
    inside_bags = bag_dict.get(bag, [])
    return "shiny-gold" in inside_bags or any(
        (gold_mine(in_bag) for in_bag in inside_bags)
    )


print(bag_dict)
print(
    """
               ,---.          _,---.          ,--.--------.                       ,---.                   
    _..---.  .--.'  \     _.='.'-,  \        /==/,  -   , -\           _..---.  .--.'  \      _,..---._   
  .' .'.-. \ \==\-/\ \   /==.'-     /        \==\.-.  - ,-./         .' .'.-. \ \==\-/\ \   /==/,   -  \  
 /==/- '=' / /==/-|_\ | /==/ -   .-'          `--`--------`         /==/- '=' / /==/-|_\ |  |==|   _   _\ 
 |==|-,   '  \==\,   - \|==|_   /_,-.         ,--.--------.         |==|-,   '  \==\,   - \ |==|  .=.   | 
 |==|  .=. \ /==/ -   ,||==|  , \_.' )       /==/,  -   , -\        |==|  .=. \ /==/ -   ,| |==|,|   | -| 
 /==/- '=' ,/==/-  /\ - \==\-  ,    (        \==\.-.  - ,-./        /==/- '=' ,/==/-  /\ - \|==|  '='   / 
|==|   -   /\==\ _.\=\.-'/==/ _  ,  /         `--`--------`        |==|   -   /\==\ _.\=\.-'|==|-,   _`/  
`-._`.___,'  `--`        `--`------'                               `-._`.___,'  `--`        `-.`.____.'   
"""
)

print(sum(gold_mine(bag) for bag in bag_dict.keys()))
