from copy import deepcopy
from common import read_file_input
from tqdm import tqdm

directions = {
    # x, y coordinates for movement
    90: (0, -1),
    180: (1, 0),
    270: (0, 1),
    360: (-1, 0)
}


def get_next_direction(d):
    if d <= 270:
        return d + 90
    return 90


def get_init_pos(m, needle):
    for i, _ in enumerate(m):
        for j, __ in enumerate(m[i]):
            if m[i][j] == needle:
                return j, i

    return -1, -1


def get_next_pos(cur_pos, d):
    x, y = cur_pos
    dx, dy = directions[d]

    return x + dx, y + dy


def simulate_guard(matrix, cur_pos):
    x, y = cur_pos
    n, m = len(matrix), len(matrix[0])
    direction = 90
    visited = set()

    while True:
        nx, ny = get_next_pos((x, y), direction)

        if ny >= n or nx >= m or nx < 0 or ny < 0:
            return False

        if matrix[ny][nx] == '#':
            direction = get_next_direction(direction)
            continue

        state = (x, y, direction)
        if state in visited:
            return True

        visited.add(state)

        # Move guard
        x, y = nx, ny

    return False

def find_obstruction_positions(matrix, guard_start):
    valid_positions = []
    n, m = len(matrix), len(matrix[0])

    for i in tqdm(range(n)):
        for j in range(m):
            if matrix[i][j] in {'#', '^'}:
                continue

            modified_matrix = deepcopy(matrix)
            modified_matrix[i][j] = '#'

            if simulate_guard(modified_matrix, guard_start):
                valid_positions.append((j,i))

    return valid_positions


if __name__ == '__main__':
    matrix = read_file_input()
    start_position = get_init_pos(matrix, '^')
    valid_positions = find_obstruction_positions(matrix, start_position)

    print(len(valid_positions))
