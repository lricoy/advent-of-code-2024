from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir / 'input.txt'

def read_file_input():
    with open(file_path, 'r') as reader:
        full_str = ''
        for line in reader:
            full_str = full_str + line.strip().rstrip("\n")

        return [full_str]