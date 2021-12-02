with open("Planned course.txt") as f:
    content = f.read()

directions = content.split("\n")
directions_array = [x.split() for x in directions]


def part1(directions):
    horizontal = 0
    depth = 0
    for direction in directions:
        magnitude = int(direction[1])

        match direction[0]:
            case "up":
                depth -= magnitude
            case "down":
                depth += magnitude
            case "forward":
                horizontal += magnitude
            case _:
                raise ValueError
    return(horizontal*depth)

print(f"Part 1: {part1(directions_array)}")

def part2(directions):
    horizontal = 0
    depth = 0
    aim = 0
    for direction in directions:
        magnitude = int(direction[1])
        match direction[0]:
            case "up":
                aim -= magnitude
            case "down":
                aim += magnitude
            case "forward":
                horizontal += magnitude
                depth += aim*magnitude
            case _:
                raise ValueError
    return(horizontal*depth)

print(f"Part 2: {part2(directions_array)}")
