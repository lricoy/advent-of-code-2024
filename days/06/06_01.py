from common import read_file_input
from pprint import pprint

directions = {
    # i, j coordinates
    90: (0, -1),
    180: (1, 0),
    270: (0, 1),
    360: (-1, 0)
}


def get_next_direction(d):
    if d <= 270:
        return d + 90
    return 90


def get_guard_position(m, needle):
    for i, _ in enumerate(m):
        for j, __ in enumerate(m[i]):
            if m[i][j] == needle:
                return j, i

    return -1, -1


def get_next_pos(cur_pos, d):
    x, y = cur_pos
    dx, dy = directions[d]

    return x + dx, y + dy


def solution(matrix, cur_pos):
    x, y = cur_pos
    n, m = len(matrix), len(matrix[0])
    direction = 90

    moves = [cur_pos]

    while True:
        nx, ny = get_next_pos(cur_pos, direction)

        if ny >= n or nx >= m or nx < 0 or ny < 0:
            return moves

        if matrix[ny][nx] == '#':
            direction = get_next_direction(direction)
            # Backtrack
            nx, ny = cur_pos

        if cur_pos != (nx, ny):
            moves.append((nx, ny, direction))
            cur_pos = nx, ny


if __name__ == '__main__':
    matrix = read_file_input('sample.txt')
    start_position = get_guard_position(matrix, '^')
    moves = solution(matrix, start_position)

    pprint(moves)

    unique_moves = set(moves)

    print(len(unique_moves))
