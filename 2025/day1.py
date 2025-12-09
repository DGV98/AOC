INPUT_PATH = "./data/day1/data.txt"


def parse(input_path):
    rotations = []
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            number = int(line[1:])
            if line[0] == "L":
                rotations.append(number * -1)
            else:
                rotations.append(number)
    return rotations


def part1(rotations):
    count = 0
    pos = 50
    for rotation in rotations:
        rotation = rotation % 100
        pos += rotation
        if pos < 0:
            pos += 100
        elif pos > 99:
            pos -= 100
        if pos == 0:
            count += 1
    return count


def part2(rotations):
    count = 0
    pos = 50
    for rotation in rotations:
        count += abs(rotation) // 100
        if rotation < 0:
            left = True
        else:
            left = False
        rotation = abs(rotation)
        rotation = rotation % 100
        if left:
            prev = pos
            pos -= rotation
            if pos <= 0:
                if prev == 0:
                    pos += 100
                else:
                    count += 1
                    if pos != 0:
                        pos += 100
        else:
            pos += rotation
            if pos > 99:
                count += 1
                pos -= 100
    return count


if __name__ == "__main__":
    rotations = parse(INPUT_PATH)
    # print(part1(rotations))
    print(part2(rotations))
