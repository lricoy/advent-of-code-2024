import os
from common import read_input_file

if __name__ == '__main__':
    list1, list2 = read_input_file()

    list1.sort()
    list2.sort()

    total_distance = sum(((abs(x - y) for x, y in zip(list1, list2))))

    print(f'The total distance is {total_distance}')
