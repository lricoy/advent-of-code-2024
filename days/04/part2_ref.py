from common import read_file_input
from typing import List
from itertools import product

def solution(matrix: List[str]):
    """
        Example:
        >>> solution(read_file_input('sample.txt'))
        9
        >>> solution(read_file_input())
        1910
    """
    n = len(matrix)
    m = len(matrix[0])
    word = 'MS'

    def is_x_at(i: int, j: int):
        if not (1 <= i < n - 1 and 1 <= j < m -1):
            return False
        if matrix[i][j] != 'A':
            return False

        diag_1 = f"{matrix[i-1][j-1]}{matrix[i+1][j+1]}"
        diag_2 = f"{matrix[i-1][j+1]}{matrix[i+1][j-1]}"

        return all(set(d) == set(word) for d in [diag_1, diag_2])


    return sum(
        is_x_at(i, j) for i, j in product(range(n), range(m))
    )

if __name__ == '__main__':
    words_found = solution(read_file_input())

    print(f"There are {words_found} X-MAS in the input")