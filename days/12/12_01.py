from pprint import pprint

with open('input.txt', 'r') as r:
    grid = [list(line.strip()) for line in r]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = len(grid), len(grid[0])
visited = set()
results = []


def bfs(start_pos):
    queue = [start_pos]
    area = []
    visited.add(start_pos)
    while queue:
        pos = queue.pop(0)
        area.append(pos)
        i, j = pos
        curr_val = grid[i][j]
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == curr_val:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return area

for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            region_positions = bfs((i, j))
            region_type = grid[i][j]
            area = len(region_positions)
            perimeter = 0

            # Calculate perimeter
            for x, y in region_positions:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != region_type:
                        perimeter += 1

            results.append((region_type, region_positions, (area, perimeter)))


for region_type, positions, (area, perimeter) in results:
    price = area * perimeter
    print(f"Region {region_type}: Area = {area}, Perimeter = {perimeter}, Price = {price}")

total_price = sum(area * perimeter for _, _, (area, perimeter) in results)
print(f"Total Price: {total_price}")
