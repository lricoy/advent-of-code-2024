from common import read_file_input
from typing import Iterable, Optional
import re


CLEAR_NON_EXECUTABLE = re.compile(
    r"""
    don't\(\)?.*?do\(\)     # Match don't()...do()
    |                       # OR
    don't\(\)(.*?)$         # Match don't() at the end of the line
    """,
    re.VERBOSE
)

FIND_MULTIPLICATIONS = re.compile(
    r"mul\(('\d{1,3}),(\d{1,3})\)" # Match mul(x,y) with 1 to 3 digits
)

def clean_line(line:str) -> str:
    executable_line, _ = CLEAR_NON_EXECUTABLE.subn("", line)
    return executable_line

def find_multiplication(line:str) -> Iterable[int]:
    for match in FIND_MULTIPLICATIONS.finditer(line):
        x, y = map(int, match.groups())
        yield x * y

def solution(input: Optional[Iterable[str]] = None) -> int:
    if input is None:
        input = read_file_input()

    return sum(
        sum(find_multiplication(clean_line(line))) for line in input
    )

if __name__ == '__main__':
    result = solution()
    print(f"The total result is {result}")