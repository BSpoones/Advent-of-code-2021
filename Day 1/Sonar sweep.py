# Puzzle input init
with open("puzzle_input.txt") as f:
    content = f.read()


depth_measurements = list(map(int,content.split("\n")))

def get_measurements(depth_measurements: list):
    current_depth = depth_measurements[0] # Starting depth
    measurements = 0
    for depth in depth_measurements[1:]:
        if depth > current_depth:
            measurements += 1
        current_depth = depth
    return measurements

print(f"Part 1: {get_measurements(depth_measurements)}")


depth_measurements_groups = []
for i,val in enumerate(depth_measurements):
    try:
        depth_measurements_groups.append([val,depth_measurements[i+1],depth_measurements[i+2]])
    except IndexError: 
        depth_measurements_groups.append(depth_measurements[i:]) # Adds all final items, even if 3 values aren't present
depth_measurements_groups_sums = [sum(x) for x in depth_measurements_groups]

print(f"Part 2: {get_measurements(depth_measurements_groups_sums)}")


import timeit
t = timeit.Timer(lambda: get_measurements(depth_measurements))
t2 = timeit.Timer(lambda: get_measurements(depth_measurements_groups_sums))
print(t.timeit(1))
print(t2.timeit(1))