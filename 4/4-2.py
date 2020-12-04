import re

with open("input.txt") as f:
    passports = f.read().split("\n\n")

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports_split = list(map(lambda x: re.split("\n| ", x), passports))
passports_split = list(
    map(lambda x: dict([tuple(i.split(":")) for i in x]), passports_split)
)


def valid_height(value):
    if re.fullmatch("[0-9]+cm$", value):
        return 150 <= int(value.split("cm")[0]) <= 193
    if re.fullmatch("[0-9]+in$", value):
        return 59 <= int(value.split("in")[0]) <= 76
    return False


valid_passports = 0
for i in passports_split:
    if any(key not in i for key in keys):
        continue
    if all(
        [
            # This is  an angry, impulsive response to failing a single test case - and, sadly, generally in keeping with my own coding standards
            re.fullmatch("[0-9]{4}", i.get("byr"))
            and (1920 <= int(i.get("byr")) <= 2002),
            re.fullmatch("[0-9]{4}", i.get("iyr"))
            and 2010 <= int(i.get("iyr")) <= 2020,
            (re.fullmatch("[0-9]{4}", i.get("eyr")))
            and 2020 <= int(i.get("eyr")) <= 2030,
            re.fullmatch("[0-9]+(cm|in)$", i.get("hgt")) and valid_height(i.get("hgt")),
            re.fullmatch(r"\#[0-9a-f]{6}", i.get("hcl")),
            re.fullmatch("[a-z]{3}", i.get("ecl"))
            and i.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            re.fullmatch("[0-9]{9}", i.get("pid")),
        ]
    ):
        valid_passports += 1


print(valid_passports)