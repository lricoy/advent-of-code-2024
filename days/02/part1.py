from common import read_input_file

def is_valid_report(report):
    """
    Validates whether a report adheres to the rules of being increasing or decreasing
    with differences of 1 to 3 between consecutive numbers.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the report is valid, False otherwise.

    Examples:
        >>> is_valid_report([7, 6, 4, 2, 1])
        True
        >>> is_valid_report([1, 2, 7, 8, 9])
        False
        >>> is_valid_report([9, 7, 6, 2, 1])
        False
        >>> is_valid_report([1, 3, 2, 4, 5])
        False
        >>> is_valid_report([8, 6, 4, 4, 1])
        False
        >>> is_valid_report([1, 3, 6, 7, 9])
        True
    """
    is_decreasing = report[0] - report[1] > 0

    for i, y in enumerate(report[1:], 1):
        x = report[i-1]
        diff = abs(x -y)
        is_valid_step = 1 <= diff <= 3

        if not is_valid_step:
            return False

        if is_decreasing and x < y or (not is_decreasing and x > y):
            return False

    return True

if __name__ == '__main__':
    valid_reports = list(filter(is_valid_report, read_input_file()))
    print(f"There are {len(valid_reports)} valid reports")