from common import read_file_input
from enum import Enum
from typing import List

class Directions(Enum):
    LEFT =(0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    UP = (-1, 0)
    DIAGONAL_DOWN_RIGHT = (1, 1)
    DIAGONAL_UP_RIGHT = (-1, 1)
    DIAGONAL_UP_LEFT = (-1, -1)
    DIAGONAL_DOWN_LEFT = (1, -1)

def solution(matrix: List[str]):
    """
        Example:
        >>> solution(read_file_input('sample.txt'))
        18
        >>> solution(read_file_input())
        2560
    """
    rows_len = len(matrix)
    cols_len = len(matrix[0])

    def is_word_at(row: int, col: int, direction: Directions, word: str):
        dr, dc = direction.value

        for i in range(len(word)):
            # Calculate the next position
            r, c = row + i * dr, col + i * dc

            # Check bounds
            if r < 0 or r >= rows_len or c < 0 or c >= cols_len:
                return False

            if matrix[r][c] != word[i]:
                return False

        return ((row, col), (r, c), direction)

    words_found = []

    for row in range(rows_len):
        for col in range(cols_len):
            for direction in Directions:
                word_coord = is_word_at(row, col, direction, "XMAS")
                if word_coord:
                    # print(word_coord)
                    words_found.append(word_coord)

    return len(words_found)

if __name__ == '__main__':
    input = read_file_input()
    words_found = solution(input)

    print(f"There are {words_found} XMAS in the input")