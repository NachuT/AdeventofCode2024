
with open("/Users/nachu/adevntofcode2024/day 5/inp.txt", "r") as file:
    lines = file.readlines()


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


from collections import defaultdict, deque

precedence = defaultdict(set)
for x, y in rules:
    precedence[x].add(y)


def topological_sort(update):

    in_degree = {page: 0 for page in update}
    local_precedence = defaultdict(set)

    for x in update:
        for y in update:
            if y in precedence[x]:
                local_precedence[x].add(y)
                in_degree[y] += 1


    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in local_precedence[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages



corrected_updates = []
for update in updates:

    position = {page: i for i, page in enumerate(update)}
    valid = True
    for x, y in rules:
        if x in position and y in position:
            if position[x] > position[y]:
                valid = False
                break

    if not valid:
        corrected_updates.append(topological_sort(update))

total = 0
for update in corrected_updates:
    middle_index = len(update) // 2
    middle_page = int(update[middle_index])
    total += middle_page

print(total)
