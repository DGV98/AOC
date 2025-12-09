INPUT = './data/day4/data.txt'


def parse(input):
    grid = []
    with open(input) as f:
        for line in f.readlines():
            line = line.strip()
            chars = []
            for char in line:
                chars.append(char)
            grid.append(chars)
    return grid


def check_perimeter(grid, x, y):
    count = 0
    n, m = len(grid), len(grid[0])
    for i in range(y-1, y + 2):
        if i < 0:
            continue
        if i >= n:
            break
        for j in range(x - 1, x + 2):
            if j < 0:
                continue
            if j >= m:
                break
            if i == y and j == x:
                continue
            if grid[i][j] == "@":
                count += 1
                if count > 3:
                    return False
    return True


def part1(grid):
    count = 0
    y = 0
    n, m = len(grid), len(grid[0])
    while y < n:
        x = 0
        while x < m:
            if grid[y][x] == "@":
                if check_perimeter(grid, x, y):
                    count += 1
            x += 1
        y += 1
    return count


def part2_helper(grid):
    count = 0
    removed = []
    y = 0
    n, m = len(grid), len(grid[0])
    while y < n:
        x = 0
        while x < m:
            if grid[y][x] == "@":
                if check_perimeter(grid, x, y):
                    count += 1
                    removed.append((x, y))
            x += 1
        y += 1
    return count, removed


def part2(grid):
    count, positions = part2_helper(grid)
    total = count
    while count != 0:
        for x, y in positions:
            grid[y][x] = "."
        count, positions = part2_helper(grid)
        total += count
    return total


if __name__ == "__main__":
    grid = parse(INPUT)
    # print(part1(grid))
    print(part2(grid))
