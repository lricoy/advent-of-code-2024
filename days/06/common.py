from pathlib import Path

script_dir = Path(__file__).resolve().parent


def read_file_input(file_name = None):
    if file_name is None:
        file_name = 'input.txt'

    file_path = script_dir / file_name

    with open(file_path, 'r') as reader:
        matrix = []

        for line in reader:
            matrix.append(list(line.rstrip("\n")))

        return matrix