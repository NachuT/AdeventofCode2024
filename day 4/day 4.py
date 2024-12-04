import re


file_path = "/Users/nachu/adevntofcode2024/day 4/inp.txt"

with open(file_path, 'r') as file:
    grid = [line.strip() for line in file]


word = "XMAS"
word_length = len(word)



def get_diagonals(grid):
    diagonals = []
    n, m = len(grid), len(grid[0])


    for d in range(-n + 1, m):
        diag = [grid[i][i - d] for i in range(max(0, d), min(n, m + d))]
        diagonals.append("".join(diag))


    for d in range(-n + 1, m):
        diag_rev = [grid[i][m - 1 - (i - d)] for i in range(max(0, d), min(n, m + d))]
        diagonals.append("".join(diag_rev))

    return diagonals



rows = grid
columns = ["".join(row[col] for row in grid) for col in range(len(grid[0]))]
diagonals = get_diagonals(grid)


all_lines = rows + columns + diagonals

total_count = 0
for line in all_lines:

    total_count += len(re.findall(rf"(?=({word}))", line))

    total_count += len(re.findall(rf"(?=({word[::-1]}))", line))

print(f"The word '{word}' appears {total_count} times.")
