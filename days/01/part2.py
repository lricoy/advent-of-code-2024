from collections import Counter
from common import IntList, read_input_file

def main():
    list1, list2 = read_input_file()

    similarity_counts = Counter(list2)

    sim_score = sum(n * similarity_counts.get(n, 0) for n in list1)

    print(f'The similarity value is {sim_score}')


if __name__ == '__main__':
    main()
