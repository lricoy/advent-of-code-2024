from common import read_file_input
from typing import  Iterable
import re

def solution(input: Iterable[str] = None):
    """
    Parses the given input, falling back to the local file (input.txt)
    if none is given and returns the total valid multiplications within.

    Examples:
        >>> solution(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])
        48
        >>> solution()
        100450138
    """
    if input is None:
        input = read_file_input()

    result = 0
    for line in input:
        # Clear the line of all non-executable operations. It is not great, but works.
        # It also considers the don't operation appearing as the last one.
        # TODO: Change the approach to a tokenizer or state/eval logic.
        executable_line, _ = re.subn(r"don't\(\)?.*?do\(\)|don't\(\)(.*?)$", "", line)

        for m in re.finditer("mul\((\d?\d?\d),(\d?\d?\d?)\)", executable_line):
            x, y = map(int, m.groups())

            result += x * y

    return result

if __name__ == '__main__':
    result = solution()

    print(f"The total result is {result}")
