with open("input.txt") as f:
    passports = f.read().split("\n\n")

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_passports = 0
for i in passports:
    if all(key + ":" in i for key in keys):
        valid_passports += 1

print(valid_passports)
