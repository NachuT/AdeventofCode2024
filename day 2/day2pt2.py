file_path = "/Users/nachu/adevntofcode2024/day 2/inp.txt"
rows_list = []

with open(file_path, "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        rows_list.append(numbers)
safe = 0

for row in rows_list:
    increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))
    valid_diff = all(1 <= abs(row[k + 1] - row[k]) <= 3 for k in range(len(row) - 1))

    if (increasing or decreasing) and valid_diff:
        safe=safe+1
    else:
        safe_after_removal = False
        for i in range(len(row)):
            modified_row = row[:i] + row[i + 1:]
            increasing = all(modified_row[j] < modified_row[j + 1] for j in range(len(modified_row) - 1))
            decreasing = all(modified_row[j] > modified_row[j + 1] for j in range(len(modified_row) - 1))
            valid_diff = all(1 <= abs(modified_row[k + 1] - modified_row[k]) <= 3 for k in range(len(modified_row) - 1))

            if (increasing or decreasing) and valid_diff:
                safe_after_removal = True
                break

        if safe_after_removal:
            safe= safe+1


print(safe)