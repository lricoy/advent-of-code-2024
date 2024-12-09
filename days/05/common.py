from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).resolve().parent


def read_file_input(file_name = None):
    if file_name is None:
        file_name = 'input.txt'

    file_path = script_dir / file_name

    rules_end = False

    rules = defaultdict(list)
    pages_to_produce = []
    with open(file_path, 'r') as reader:
        for line in reader:
            if line == '\n':
                rules_end = True
                continue

            line = line.rstrip('\n')

            if rules_end:
                pages_to_produce.append(line.split(','))
            else:
                before, after = line.split('|')
                rules[before].append(after)

        return rules, pages_to_produce

