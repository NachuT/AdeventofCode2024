# Read the file
with open("/Users/nachu/adevntofcode2024/day 5/inp.txt", "r") as file:
    lines = file.readlines()

# Separate rules and updates
rules = []
updates = []
reading_updates = False
for line in lines:
    line = line.strip()
    if not line:
        reading_updates = True
        continue
    if reading_updates:
        updates.append(line.split(","))
    else:
        x, y = line.split("|")
        rules.append((x, y))

# Parse rules into a precedence graph
from collections import defaultdict, deque

precedence = defaultdict(set)
for x, y in rules:
    precedence[x].add(y)


# Helper function to topologically sort the pages in an update
def topological_sort(update):
    in_degree = {page: 0 for page in update}
    for x in update:
        for y in update:
            if y in precedence[x]:
                in_degree[y] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in update:
            if neighbor in precedence[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return sorted_pages


# Check and correct updates
corrected_updates = []
for update in updates:
    # Build a dictionary of positions
    position = {page: i for i, page in enumerate(update)}
    valid = True
    for x, y in rules:
        if x in position and y in position:
            if position[x] > position[y]:  # Invalid order
                valid = False
                break

    if not valid:
        corrected_updates.append(topological_sort(update))

# Find middle pages and calculate the sum
total = 0
for update in corrected_updates:
    middle_index = len(update) // 2
    middle_page = int(update[middle_index])
    total += middle_page

print(total)
