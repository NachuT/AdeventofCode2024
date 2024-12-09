def calculate_compaction_simple(data):
    disk_map = []
    for i in range(0, len(data), 2):
        file_id = i // 2
        disk_map.extend([file_id] * int(data[i]))
        if i + 1 < len(data):
            disk_map.extend(['.'] * int(data[i + 1]))

    left_pointer = 0
    right_pointer = len(disk_map) - 1

    while left_pointer < right_pointer:
        while disk_map[left_pointer] != '.' and left_pointer < len(disk_map):
            left_pointer += 1
        while disk_map[right_pointer] == '.' and right_pointer >= 0:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break

        disk_map[left_pointer], disk_map[right_pointer] = (
            disk_map[right_pointer],
            disk_map[left_pointer],
        )

    checksum = sum(
        index * int(block) for index, block in enumerate(disk_map) if block != '.'
    )
    return checksum


if __name__ == "__main__":
    input_file = "/day 9/inp.txt"
    with open(input_file, "r") as file:
        disk_data = file.read().strip()

    result = calculate_compaction_simple(disk_data)
    print(result)
