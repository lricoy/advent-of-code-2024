from concurrent.futures.process import ProcessPoolExecutor
import os
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


def get_guard_og_path(matrix, cur_pos):
    x, y = cur_pos
    n, m = len(matrix), len(matrix[0])
    direction = 90

    visited = {cur_pos}

    while True:
        nx, ny = get_next_pos(cur_pos, direction)

        if ny >= n or nx >= m or nx < 0 or ny < 0:
            return visited

        if matrix[ny][nx] == '#':
            direction = get_next_direction(direction)
            # Backtrack
            nx, ny = cur_pos

        if cur_pos != (nx, ny):
            visited.add((nx, ny))
            cur_pos = nx, ny


def proccess_guard_path(matrix, guard_start, guard_path):
    valid_positions = []

    for x, y in tqdm(guard_path):
        if matrix[y][x] in {'#', '^'}:
            continue

        og_val = matrix[y][x]
        matrix[y][x] = '#'

        if simulate_guard(matrix, guard_start):
            valid_positions.append((x, y))

        matrix[y][x] = og_val

    return valid_positions


def find_obstruction_positions(matrix, guard_start):
    guard_path = list(get_guard_og_path(matrix, guard_start))

    num_workers = os.cpu_count()

    chunk_size = len(guard_path) // num_workers
    path_chunks = [guard_path[i: i + chunk_size] for i in range(0, len(guard_path), chunk_size)]

    valid_positions = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [
            executor.submit(proccess_guard_path, matrix, guard_start, chunk) for chunk in path_chunks
        ]

        for future in tqdm(futures):
            valid_positions.extend(future.result())

    return valid_positions


if __name__ == '__main__':
    matrix = read_file_input()
    start_position = get_init_pos(matrix, '^')
    valid_positions = find_obstruction_positions(matrix, start_position)

    print(len(valid_positions))
