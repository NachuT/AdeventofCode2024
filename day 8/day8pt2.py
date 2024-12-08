import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

file_path = sys.argv[1] if len(sys.argv) >= 2 else '/Users/nachu/adevntofcode2024/day 8/inp.txt'

data = open(file_path).read().strip()
grid = data.split('\n')

num_rows = len(grid)
num_cols = len(grid[0])

positions = defaultdict(list)
for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] != '.':
            positions[grid[row][col]].append((row, col))

set_part2 = set()

for row in range(num_rows):
    for col in range(num_cols):
        for char, coords in positions.items():
            for (r1, c1) in coords:
                for (r2, c2) in coords:
                    if (r1, c1) != (r2, c2):
                        distance1 = abs(row - r1) + abs(col - c1)
                        distance2 = abs(row - r2) + abs(col - c2)

                        delta_r1 = row - r1
                        delta_r2 = row - r2
                        delta_c1 = col - c1
                        delta_c2 = col - c2

                        if 0 <= row < num_rows and 0 <= col < num_cols and (delta_r1 * delta_c2 == delta_c1 * delta_r2):
                            set_part2.add((row, col))

result_part2 = len(set_part2)
print(result_part2)
