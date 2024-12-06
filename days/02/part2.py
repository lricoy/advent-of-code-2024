from common import read_input_file
from typing import List

def is_valid_step(x: int, y: int, is_decreasing: bool) -> bool:
    diff = abs(x - y)
    return (
        1 <= diff <= 3 and
        ((is_decreasing and x >= y) or (not is_decreasing and x <= y))
    )

def is_decreasing_trend(report: List[int]) -> bool:
    return report[0] > report[1]

def is_valid_report(report: List[int]):
    is_decreasing = is_decreasing_trend(report)
    return all(is_valid_step(x, y, is_decreasing) for x, y in zip(report, report[1:]))

def validate_dampened_report(report: List[int]) -> bool:
    """
    Validates whether a report is valid, allowing for one dampened level to be removed.

    Args:
        report (List[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the report is valid or becomes valid after removing one level.

    Examples:
        >>> validate_dampened_report([7, 6, 4, 2, 1])
        True
        >>> validate_dampened_report([1, 2, 7, 8, 9])
        False
        >>> validate_dampened_report([9, 7, 6, 2, 1])
        False
        >>> validate_dampened_report([1, 3, 2, 4, 5])
        True
        >>> validate_dampened_report([8, 6, 4, 4, 1])
        True
        >>> validate_dampened_report([1, 3, 6, 7, 9])
        True
    """
    if is_valid_report(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_valid_report(modified_report):
            return True

    return False

if __name__ == '__main__':
    reports = read_input_file()

    valid_reports = [report for report in reports if validate_dampened_report(report)]

    print(f"There are {len(valid_reports)} valid reports")