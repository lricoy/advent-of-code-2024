from common import read_file_input
from graphlib import TopologicalSorter


def build_graph(rules, pages):
    return {page: [v for v in rules.get(page, []) if v in pages] for page in pages}


def is_valid_order(graph, order):
    for i, page in enumerate(order):
        pages = graph.get(page, [])
        if any(successor in order[:i] for successor in pages):
            return False
    return True


def reorder(graph):
    return list(TopologicalSorter(graph).static_order())


def solution(rules, pages_to_produce):
    corrected_orders = []

    for order in pages_to_produce:
        graph = build_graph(rules, order)

        if not is_valid_order(graph, order):
            corrected = reorder(build_graph(rules, order))
            corrected_orders.append(corrected)

    return corrected_orders


if __name__ == '__main__':
    rules, pages_to_produce = read_file_input()
    corrected_ops = solution(rules, pages_to_produce)

    result = sum(int(op[len(op) // 2]) for op in corrected_ops)

    print(result)
