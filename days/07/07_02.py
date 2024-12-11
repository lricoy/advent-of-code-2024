from collections import defaultdict
from itertools import product

operations = []
with open('input.txt', 'r') as reader:
    for line in reader:
        total, exp = line.strip().split(':')
        operations.append((total, exp.strip()))


total = 0
for result, exp in operations:
    result = int(result)

    for comb in  product('* + ||'.split(' '), repeat=len(exp.split(' ')) -1):
        operands = list(map(int, exp.split(' ')))
        eval_result = operands.pop(0)

        for operator in comb:
            if operator == '+':
                eval_result += operands.pop(0)
            elif operator == '||':
                eval_result = int(f'{eval_result}{operands.pop(0)}')
            else:
                eval_result *= operands.pop(0)

        if eval_result == result:
            total += result
            break


print(total)