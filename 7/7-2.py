import re
from collections import defaultdict

with open("input.txt") as f:
    bag_list = f.read().split("\n")

identify_bag = re.compile(r"([0-9]?) *([a-z]*)? ([a-z]*)? bag[s]?")
identify_no_bags = re.compile(r"([a-z]*)? ([a-z]*)? bag[s]? contain no other bags")
bag_dict = defaultdict(list)

for j in bag_list:
    key_bag = ""
    child_bags = []
    for i in re.findall(identify_bag, j):
        if i[0] == "":
            key_bag = i[1] + "-" + i[2]
        else:
            child_bags.append((i[1] + "-" + i[2], int(i[0])))
    children = dict(child_bags)
    bag_dict[key_bag] = children


def count_gold_mine(bag, count):
    if bag_dict[bag] == []:
        return 1
    return 1 + sum(
        count * count_gold_mine(thisbag, count)
        for thisbag, count in bag_dict[bag].items()
    )


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

print(count_gold_mine("shiny-gold", 1) - 1)