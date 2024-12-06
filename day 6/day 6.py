directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open('/Users/nachu/adevntofcode2024/day 6/inp.txt', 'r') as file:
    grid = file.read().splitlines()

lab = [list(row) for row in grid]

start_pos = None
start_dir = None
for i, row in enumerate(lab):
    for j, cell in enumerate(row):
        if cell == '^':
            start_pos = (i, j)
            start_dir = 0
            lab[i][j] = '.'
        elif cell == '>':
            start_pos = (i, j)
            start_dir = 1
            lab[i][j] = '.'
        elif cell == 'v':
            start_pos = (i, j)
            start_dir = 2
            lab[i][j] = '.'
        elif cell == '<':
            start_pos = (i, j)
            start_dir = 3
            lab[i][j] = '.'

visited = set()
y, x = start_pos
direction = start_dir
visited.add((y, x))

while True:
    dy, dx = directions[direction]
    new_y, new_x = y + dy, x + dx

    if not (0 <= new_y < len(lab) and 0 <= new_x < len(lab[0])):
        break

    if lab[new_y][new_x] == '#':
        direction = (direction + 1) % 4
    else:
        y, x = new_y, new_x
        visited.add((y, x))

print(len(visited))
