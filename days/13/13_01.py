from pprint import pprint
from math import gcd

with open('input.txt') as reader:
    machines = [m.split('\n') for m in reader.read().strip().split('\n\n')]
    parsed_machines = []
    for m in machines:
        prize = int(m[2][m[2].index('=') + 1: m[2].index(',')]), int(m[2][m[2].index('=', m[2].index(',')) + 1: len(m[2])])
        a = int(m[0][m[0].index('+') + 1: m[0].index(',')]), int(m[0][m[0].index('+', m[0].index(',')) + 1: len(m[0])])
        b = int(m[1][m[1].index('+') + 1: m[1].index(',')]), int(m[1][m[1].index('+', m[1].index(',')) + 1: len(m[1])])

        parsed_machines.append((a, b, prize))


def is_reachable(machine):
    a, b, prize = machine

    ax, ay = a
    bx, by = b
    px, py = prize

    return px % gcd(ax, bx) == 0 and py % gcd(ay, by) == 0

def min_cost(machine):
    a, b, prize = machine
    ax, ay = a
    bx, by = b
    px, py = prize

    min_cost = float('inf')

    for n in range(1, 100):
        for m in range (1, 100):
            if n * ax + m * bx == px and n * ay + m * by == py:
                cost = 3 * n + m
                min_cost = min(min_cost, cost)

    return min_cost if min_cost != float('inf') else None

tokens = []
for m in parsed_machines:
    if is_reachable(m):
        tokens.append(min_cost(m))

print(sum(t for t in tokens if t is not None))