import re


file_path = "/Users/nachu/adevntofcode2024/day 3/inp.txt"
with open(file_path, 'r') as file:
    content = file.read()

pattern = r"mul\((\d*),(\d*)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
result=0
active=True
for instruction in re.finditer(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", content):
    match = instruction.group()

    if match=="do()":
        active=True
    elif match=="don't()":
        active=False
    elif "mul" in match and active:
        a, b = re.findall(r"\d+", match)
        result += int(a) * int(b)

print(result)