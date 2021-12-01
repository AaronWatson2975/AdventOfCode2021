puzzle_input_file = open("puzzle_input.txt", "r")
lines = puzzle_input_file.readlines()
number_arr = [int(numeric_string) for numeric_string in lines]

increased_depth = 0

for idx, depth in enumerate(number_arr):
    if(idx == 0):
        continue
    previous_depth = number_arr[idx-1]
    if(depth > previous_depth):
        increased_depth += 1


print(f"Total readings: {len(number_arr)}")
print(f"Total increases: {increased_depth}")
