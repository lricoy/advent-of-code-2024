from pprint import pprint

with open('input.txt') as reader:
    grid = []
    for line in reader:
        grid.append(list(map(int, line.strip())))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = len(grid), len(grid[0])


def find_start_positions():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                yield i, j


def find_next_steps(pos):
    i, j = pos
    curr_val = grid[i][j]
    next_values = []
    for x, y in directions:
        if 0 <= x + i < n and 0 <= y + j < m:
            if grid[x + i][y + j] == curr_val + 1:
                next_values.append((x + i, y + j))

    return next_values

def print_trail(grid, visited):
    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                print(grid[i][j], end='')
            else:
                print('.', end='')
        print()
    print('***' * 20)


starts = list(find_start_positions())

trailhead_scores = []

for start in starts:
    visited = set()
    # Shoul've used DFS from the start, but wanted to practice
    q = [start]
    trailhead_count = 0
    while q:
        val = q.pop(0)

        if val in visited:
            continue
        visited.add(val)

        if grid[val[0]][val[1]] == 9:
            trailhead_count += 1

        q.extend(find_next_steps(val))
        # print(q)

    trailhead_scores.append(trailhead_count)

print(sum(trailhead_scores))
