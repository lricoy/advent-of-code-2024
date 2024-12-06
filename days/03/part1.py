from common import read_file_input
from typing import  Iterable
import re

def solution(input: Iterable[str] = None):
    """
    Parses the given input, falling back to the local file (input.txt)
    if none is given and returns the total valid multiplications within.

    Examples:
        >>> solution(["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"])
        161
    """
    if input is None:
        input = read_file_input()

    result = 0
    for line in input:

        for m in re.finditer("mul\((\d?\d?\d),(\d?\d?\d?)\)", line):
            x, y = map(int, m.groups())

            result += x * y

    return result

if __name__ == '__main__':
    result = solution()

    print(f"The total result is {result}")
