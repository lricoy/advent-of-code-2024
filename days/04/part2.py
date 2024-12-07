from common import read_file_input
from enum import Enum
from typing import List

class Directions(Enum):
    DIAGONAL_DOWN_RIGHT = (1, 1)
    DIAGONAL_UP_RIGHT = (-1, 1)
    DIAGONAL_UP_LEFT = (-1, -1)
    DIAGONAL_DOWN_LEFT = (1, -1)

class Diagonals(Enum):
    LEFT = (Directions.DIAGONAL_UP_LEFT, Directions.DIAGONAL_DOWN_RIGHT)
    RIGHT = (Directions.DIAGONAL_UP_RIGHT, Directions.DIAGONAL_DOWN_LEFT)

def solution(matrix: List[str]):
    """
        Example:
        >>> solution(read_file_input('sample.txt'))
        9
        >>> solution(read_file_input())
        1910
    """
    rows_len = len(matrix)
    cols_len = len(matrix[0])

    def is_x_at(row: int, col: int, word: str):
        chars = {
            Diagonals.LEFT.name: set(),
            Diagonals.RIGHT.name: set()
        }

        for d in Diagonals:
            for dr, dc in [v.value for v in list(d.value)]:
                r, c = row + dr, col + dc

                # Check bounds
                if r < 0 or r >= rows_len or c < 0 or c >= cols_len:
                    return False

                chars[d.name].add(matrix[r][c])

        if all(set(c) == set(word) for c in chars.values()):
            return (row, col)

        return False

    exes_found = []

    for row in range(rows_len):
        for col in range(cols_len):
            if matrix[row][col] == 'A':
                word_coord = is_x_at(row, col, "MS")
                if word_coord:
                    exes_found.append(word_coord)

    return len(exes_found)

if __name__ == '__main__':
    words_found = solution(read_file_input())

    print(f"There are {words_found} X-MAS in the input")