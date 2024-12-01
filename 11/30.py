
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

left_numbers.sort()
right_numbers.sort()
overall_total = 0
length=len(left_numbers)

for i in range(length):
    running_total=abs(left_numbers[i] - right_numbers[i])
    overall_total= running_total+overall_total
print(overall_total)



