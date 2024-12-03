import re


file_path = "/Users/nachu/adevntofcode2024/day 3/inp.txt"
with open(file_path, 'r') as file:
    content = file.read()

pattern = r"mul\((\d*),(\d*)\)"
matches = re.findall(pattern, content)
result = sum(int(a) * int(b) for a, b in matches)

print(result)
