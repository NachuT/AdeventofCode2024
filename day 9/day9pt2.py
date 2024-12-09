import heapq


def calculate_compaction_with_priority(data):
    disk_map = []
    free_blocks = []
    file_locations = []

    for i in range(0, len(data), 2):
        file_id = i // 2
        previous_position = len(disk_map)
        disk_map.extend([file_id] * int(data[i]))
        heapq.heappush(
            file_locations,
            (-file_id, len(disk_map) - previous_position, previous_position),
        )
        if i + 1 < len(data):
            start_free = len(disk_map)
            disk_map.extend(['.'] * int(data[i + 1]))
            heapq.heappush(
                free_blocks,
                (start_free, len(disk_map) - start_free),
            )

    while file_locations:
        file_id, file_length, file_position = heapq.heappop(file_locations)
        for index, (start_free, free_length) in enumerate(free_blocks):
            if file_length <= free_length and start_free < file_position:
                for i in range(start_free, start_free + file_length):
                    disk_map[i] = -file_id
                    disk_map[file_position] = '.'
                    file_position += 1

                if free_length > file_length:
                    free_blocks[index] = (
                        start_free + file_length,
                        free_length - file_length,
                    )
                else:
                    del free_blocks[index]
                break

    checksum = sum(
        index * int(block) for index, block in enumerate(disk_map) if block != '.'
    )
    return checksum


if __name__ == "__main__":
    input_file = "/day 9/inp.txt"
    with open(input_file, "r") as file:
        disk_data = file.read().strip()

    result = calculate_compaction_with_priority(disk_data)
    print(result)
