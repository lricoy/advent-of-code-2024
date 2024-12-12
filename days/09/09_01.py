from pprint import pprint

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


end = False
i = len(broad_disk) - 1
while not end:
    og_value = broad_disk[i]
    has_space = True
    # print(broad_disk)

    for j in range(i):
        if broad_disk[j] == '.':
            broad_disk[j] = og_value
            broad_disk[i] = '.'
            i -= 1
            break
    else:
        end = True


print(broad_disk)

checksum = sum( i * v for i,v in enumerate(broad_disk) if v != '.')
pprint(checksum)