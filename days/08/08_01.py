from collections import defaultdict
from pprint import pprint
import re

with open('input.txt') as reader:
    grid = []
    for line in reader:
        grid.append(list(line.strip()))


def find_antennas(matrix):
    ant_map = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if re.match(r'[a-z]|[A-Z]|[0-9]', matrix[i][j]):
                ant_map[matrix[i][j]].append((i,j))
    return ant_map

def get_pairs(antenas):
    antinodes = []
    for i in range(len(antenas)):
        for j in range(i + 1, len(antenas)):
            antinodes.extend(calc_antinodes(antenas[i], antenas[j]))
    return antinodes

def calc_antinodes(a1, a2):
    x1, y1 = a1
    x2, y2 = a2

    cx, cy = x1 - (x2 - x1), y1 - (y2 - y1)
    dx, dy = x2 + (x2 - x1), y2 + (y2 - y1)

    yield cx, cy
    yield dx, dy


antennas = find_antennas(grid)
all_antinodes = set()

m, n = len(grid), len(grid[0])

for freq, position in antennas.items():
    antinode_pairs = get_pairs(position)
    for pair in antinode_pairs:
        x, y = pair
        if 0 <= y < n and  0 <= x < m:
            all_antinodes.add(pair)

print("Total unique antinode positions:", len(all_antinodes))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in all_antinodes:
            grid[i][j] = '#'
for row in grid:
    print(''.join(row))