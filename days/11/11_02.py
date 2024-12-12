with open('input.txt', 'r') as r:
    stone_list = list(map(int, r.read().strip().split()))

cache = {}


def evolve_single_stone(x, n):
    if n == 0:
        return 1

    result = 0

    if (x, n) not in cache:
        if x == 0:
            result = evolve_single_stone(1, n - 1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            mid = len(s) // 2
            left, right = int(s[:mid]), int(s[mid:])
            result += evolve_single_stone(left, n - 1)
            result += evolve_single_stone(right, n - 1)
        else:
            result = evolve_single_stone(2024 * x, n - 1)
        cache[(x, n)] = result

    return cache[(x, n)]


if __name__ == '__main__':
    res = 0
    for stone in stone_list:
        res += evolve_single_stone(stone, 75)

    print(f"Cache is holding {len(cache)} elements")
    print(f"Total number of stones: {res}")
