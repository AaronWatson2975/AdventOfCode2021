puzzle_input_file = open("puzzle_input.txt", "r")
lines = puzzle_input_file.readlines()
number_arr = [int(numeric_string) for numeric_string in lines]

increases = 0
windows = []

for idx, depth in enumerate(number_arr):
    if(idx < 2):
        continue
    windows.append(sum(number_arr[idx-2:idx+1]))

for idx, window in enumerate(windows):
    if(idx == 0):
        continue
    previous_window = windows[idx-1]
    if(window > previous_window):
        increases += 1

print(f"Total windows: {len(windows)}")
print(f"Total increases: {increases}")
