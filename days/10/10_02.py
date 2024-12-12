from pprint import pprint

with open('sample.txt') as reader:
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


def is_valid_move(grid, x, y, nx, ny, visited):
    if 0 <= nx < n and 0 <= ny < m:
        if (nx, ny) not in visited:
            if grid[nx][ny] == grid[x][y] + 1:
                return True

    return False


def dfs(grid, x, y, visited, current_path):
    if grid[x][y] == 9:
        # print_trail(grid, visited)
        return 1

    visited.add((x, y))

    distinct_trails = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(grid, x, y, nx, ny, visited):
            distinct_trails += dfs(grid, nx, ny, visited, current_path + [(nx, ny)])

    visited.remove((x, y))
    return distinct_trails


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

scores = []
for start in starts:
    distinct_paths = dfs(grid, start[0], start[1], set(), [])
    scores.append(distinct_paths)

print(scores)
print(sum(scores))
