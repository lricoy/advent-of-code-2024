from typing import Tuple, List
from pathlib import Path

IntList = List[int]

script_dir = Path(__file__).resolve().parent
file_path = script_dir / 'input.txt'

def read_input_file() -> Tuple[IntList, IntList]:
    list1: IntList = []
    list2: IntList = []

    with open(file_path, 'r') as reader:
        for line in reader:
            n1, n2 = map(int, line.strip().split('   '))
            list1.append(n1)
            list2.append(n2)

    return list1, list2
