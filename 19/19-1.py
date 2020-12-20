import re

with open("input.txt") as f:
    splits = f.read().split("\n\n")

all_rules = splits[0].replace("\n", " \n")
rules = [r for r in all_rules.split("\n")]
messages = splits[1]

rules_dict = {}

for i in rules:
    number, rule = i.split(":")
    if '"' in rule:
        rule = rule.replace('"', "")
    rules_dict[number] = rule


for x in range(15):
    for k in rules_dict:
        # all_rules = re.sub(rf"{k}(?!:)", rf"({rules_dict[k]})", all_rules)
        all_rules = re.sub(rf" \b{k}\b ", rf" ({rules_dict[k]} ) ", all_rules)

zero = re.match(r"0:.*\n", all_rules)[0].split(":")[1]
print(zero)
zero = zero.replace(" ", "").replace("(a)", "a").replace("(b)", "b")
matches = 0

print(len(re.findall(rf"\b{zero}\b", messages)) + 1)