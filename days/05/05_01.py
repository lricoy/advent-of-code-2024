from common import read_file_input


def solution(rules, pages_to_produce):
    valid_orders = []

    for order in pages_to_produce:
        rules_to_consider = {k:v for k,v in rules.items() if k in order}

        invalid_pages = 0
        for i, page in enumerate(order):
            page_rules = rules_to_consider.get(page, [])

            is_valid = set(order[i + 1:]).issubset(set(page_rules))

            if not is_valid:
                invalid_pages += 1

        if invalid_pages == 0:
            valid_orders.append(order)

    return valid_orders

if __name__ == '__main__':
    rules, page_to_produce = read_file_input()
    valid_operations = solution(rules, page_to_produce)


    result = sum(int(op[len(op)//2]) for op in valid_operations)

    print(result)