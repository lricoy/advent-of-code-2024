from collections import deque

cache = {}


def evolve_single_stone_iterative(stone, n):
    if (stone, n) in cache:
        return cache[(stone, n)]

    stack = deque([(stone, n)])
    results = {}

    while stack:
        current, remaining = stack.pop()

        if remaining == 0:
            results[(current, remaining)] = 1
            continue

        if (current, remaining) in results:
            continue

        if current == 0:
            dep = (1, remaining - 1)
            if dep in results:
                results[(current, remaining)] = results[dep]
            else:
                stack.extend([(current, remaining), dep])
        elif len(str(current)) % 2 == 0:
            s = str(current)
            mid = len(s) // 2
            left, right = int(s[:mid]), int(s[mid:])
            deps = [(left, remaining - 1), (right, remaining - 1)]
            if all(dep in results for dep in deps):
                results[(current, remaining)] = sum(results[dep] for dep in deps)
            else:
                stack.extend([(current, remaining)] + deps)
        else:
            dep = (current * 2024, remaining - 1)
            if dep in results:
                results[(current, remaining)] = results[dep]
            else:
                stack.extend([(current, remaining), dep])

    cache.update(results)
    return results[(stone, n)]


if __name__ == '__main__':
    with open('input.txt', 'r') as r:
        stone_list = list(map(int, r.read().strip().split()))
    iterations = 75
    print(sum(evolve_single_stone_iterative(stone, iterations) for stone in stone_list))
