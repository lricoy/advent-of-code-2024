with open('input.txt', 'r') as r:
    stone_list = list(map(int, r.read().strip().split()))

def apply_rules(stone):
    if stone == 0:
        return 1

    s = str(stone)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        left, right = s[:mid], s[mid:]
        return [int(left), int(right)]

    return stone * 2024


def blink(iterations, stone_list):
    for n in range(iterations):
        new_list = []
        for i, stone in enumerate(stone_list):
            new_stone = apply_rules(stone)
            if isinstance(new_stone, list):
                new_list.extend(new_stone)
            else:
                new_list.append(new_stone)
        # print(f'After {n + 1} blinks')
        # print(new_list)
        stone_list = new_list

    print(len(stone_list))

if __name__ == '__main__':
    iterations = 25
    blink(iterations, stone_list)