
file_path = "/Users/nachu/adevntofcode2024/day 4/inp.txt"


with open(file_path, 'r') as file:
    grid = [line.strip() for line in file]


target_words = {"MAS", "SAM"}


def count_x_mas(grid, row, col):
    n, m = len(grid), len(grid[0])
    count = 0


    if not (1 <= row < n - 1 and 1 <= col < m - 1):
        return 0
    top_left = grid[row - 1][col - 1]
    top_right = grid[row - 1][col + 1]
    center = grid[row][col]
    bottom_left = grid[row + 1][col - 1]
    bottom_right = grid[row + 1][col + 1]

    diag_1 = top_left + center + bottom_right
    diag_2 = top_right + center + bottom_left

    if diag_1 in target_words and diag_2 in target_words:
        count += 1

    return count


total_count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        total_count += count_x_mas(grid, row, col)

print(total_count)
