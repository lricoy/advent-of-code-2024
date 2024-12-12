from pprint import pprint
from tqdm import tqdm

with open('input.txt') as input_file:
    disk_map = list(map(int, list(input_file.read().strip())))

# Initialize broad disk and unique identifier for non-empty blocks
broad_disk_representation = []
unique_block_id = 0

# Populate broad disk representation based on disk_map
for index in range(len(disk_map)):
    if index % 2 == 0:
        for _ in range(disk_map[index]):
            broad_disk_representation.append(unique_block_id)
        unique_block_id += 1
    else:
        for _ in range(disk_map[index]):
            broad_disk_representation.append('.')

# Start processing the disk from the end
current_index = len(broad_disk_representation) - 1

with tqdm(total=current_index + 1, unit="step") as progress_bar:
    while current_index >= 0:
        if broad_disk_representation[current_index] == '.':
            current_index -= 1
            progress_bar.update(1)
            continue

        current_block_id = broad_disk_representation[current_index]

        # Find the start of the current block
        block_start_index = current_index
        while block_start_index >= 0 and broad_disk_representation[block_start_index] == current_block_id:
            block_start_index -= 1
        block_start_index += 1  # Adjust back to the first occurrence

        block_size = current_index - block_start_index + 1

        # Try to move the block to the left
        for left_index in range(block_start_index):
            if broad_disk_representation[left_index] == '.':
                gap_index = left_index
                while broad_disk_representation[gap_index] == '.':
                    gap_index += 1

                if gap_index - left_index >= block_size:
                    # Move block to the gap
                    for replacement_index in range(left_index, left_index + block_size):
                        broad_disk_representation[replacement_index] = current_block_id

                    # Clear the original block position
                    for clear_index in range(block_start_index, current_index + 1):
                        broad_disk_representation[clear_index] = '.'

                    break

        current_index = block_start_index - 1
        progress_bar.update(1)

# Calculate checksum based on the final state of the disk
checksum = sum(index * value for index, value in enumerate(broad_disk_representation) if value != '.')
pprint(checksum)