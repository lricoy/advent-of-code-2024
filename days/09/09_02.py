from pprint import pprint
from tqdm import tqdm

with open('input.txt') as fin:
    disk_map = list(map(int, list(fin.read().strip())))


broad_disk = []
id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        for j in range(disk_map[i]):
            broad_disk.append(id)
        id += 1
    else:
        for j in range(disk_map[i]):
            broad_disk.append('.')


i = len(broad_disk) - 1
with tqdm(total=i + 1, unit="step") as pbar:
    while i >= 0:
        if broad_disk[i] == '.':
            i -= 1
            pbar.update(1)
            continue

        og_value = broad_disk[i]

        i2 = i
        while i2 >= 0 and broad_disk[i2] == og_value:
            i2 -= 1
        i2 += 1 # Adjust back to the first occurrence

        file_size = i - i2 + 1

        for j in range(i2):

            if broad_disk[j] == '.':
                jj = j
                while broad_disk[jj] == '.':
                    jj += 1

                if jj - j >= file_size:

                    for k in range(j, j + file_size):
                        broad_disk[k] = og_value

                    for k in range(i2, i + 1):
                        broad_disk[k] = '.'

                    # print(''.join([str(x) for x in broad_disk]))
                    # print(i,j)
                    break

        i = i2 - 1
        pbar.update(1)



checksum = sum( i * v for i,v in enumerate(broad_disk) if v != '.')
pprint(checksum)