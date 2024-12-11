from collections import defaultdict
import re

ANTENNA_PATTERN = re.compile(r'[a-zA-Z0-9]')

def read_grid(filename):
    with open(filename) as reader:
        return [list(line.strip()) for line in reader]

def find_antennas(matrix):
    ant_map = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Considering this is advent of code, we could just
            # do the opposite and check for != "."
            if ANTENNA_PATTERN.match(matrix[i][j]):
                ant_map[matrix[i][j]].append((i,j))
    return ant_map

def is_within_board(x: int, y: int, n, m):
    return 0 <= y < n and 0 <= x < m

def generate_nodes(a1, a2, n, m):
    x1, y1 = a1
    x2, y2 = a2
    dx, dy = x2 - x1, y2 - y1

    for direction in (1, -1):
        i = 0
        while True:
            nx, ny = x1 - dx * i * direction, y1 - dy * i * direction
            if is_within_board(nx, ny, n, m):
                yield nx, ny
            else:
                break
            i += 1

def get_pairs(antenas, n, m):
    antinodes = []
    for i in range(len(antenas)):
        for j in range(i + 1, len(antenas)):
            antinodes.extend(generate_nodes(antenas[i], antenas[j], n, m))
    return antinodes

def print_board(grid, antinodes):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in antinodes:
                grid[i][j] = '#'
    for row in grid:
        print(''.join(row))


def find_all_antinodes(grid):
    antennas = find_antennas(grid)
    all_antinodes = set()
    n, m = len(grid), len(grid[0])

    for freq, position in antennas.items():
        antinode_pairs = get_pairs(position, n, m)
        for pair in antinode_pairs:
            all_antinodes.add(pair)

    return all_antinodes

def main():
    grid = read_grid('input.txt')
    all_antinodes = find_all_antinodes(grid)
    print_board(grid, all_antinodes)
    print("Total unique antinode positions:", len(all_antinodes))

if __name__ == '__main__':
    main()
