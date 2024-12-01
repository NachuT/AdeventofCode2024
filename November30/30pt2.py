
input_file = "/11/inp.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

left_numbers = []
right_numbers = []

for line in lines:
    parts = line.split()
    if len(parts) == 2:
        left_numbers.append(int(parts[0]))
        right_numbers.append(int(parts[1]))

overall_total = 0
length=len(left_numbers)


for i in range(length):
    indices = [t for t, x in enumerate(right_numbers) if x == left_numbers[i]]
    n_index = len(indices)
    running_total=n_index*left_numbers[i]
    overall_total=overall_total+running_total
print(overall_total)


