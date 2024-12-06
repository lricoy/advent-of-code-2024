from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir / 'input.txt'

def read_input_file():
    with open(file_path, 'r') as reader:
        for line in reader:
            yield list(map(int, line.strip().split(' ')))