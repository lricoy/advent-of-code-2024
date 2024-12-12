from collections import deque

def calculate_dependencies(current, remaining):
    if current == 0:
        return [(1, remaining - 1)]
    elif len(str(current)) % 2 == 0:
        s = str(current)
        left, right = int(s[:len(s)//2]), int(s[len(s)//2:])
        return [(left, remaining - 1), (right, remaining - 1)]
    else:
        return [(current * 2024, remaining - 1)]

def resolve_dependencies(dependencies, results):
    return sum(results[dep] for dep in dependencies)

def evolve_single_stone_iterative(stone, n):
    results = {}
    stack = deque([(stone, n)])

    while stack:
        current, remaining = stack.pop()

        if remaining == 0:
            results[(current, remaining)] = 1
            continue

        if (current, remaining) in results:
            continue

        # Calculate dependencies for the current state
        dependencies = calculate_dependencies(current, remaining)

        # If all dependencies are resolved, compute the result
        if all(dep in results for dep in dependencies):
            results[(current, remaining)] = resolve_dependencies(dependencies, results)
        else:
            # Push the current state back into the stack along with unresolved dependencies
            stack.extend([(current, remaining)] + dependencies)

    return results[(stone, n)]

def compute_stone_count(stone_list, iterations):
    return sum(evolve_single_stone_iterative(stone, iterations) for stone in stone_list)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        stone_list = list(map(int, file.read().strip().split()))
    iterations = 75
    stone_count = compute_stone_count(stone_list, iterations)
    print(stone_count)
