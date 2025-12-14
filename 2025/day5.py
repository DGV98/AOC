INPUT = 'data/day5/data.txt'


def parse(path):
    ranges = []
    ids = []
    new_line_flag = False
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                new_line_flag = True
                continue
            if new_line_flag:
                ids.append(int(line))
            else:
                lo, hi = line.split("-")
                ranges.append((int(lo), int(hi)))
    return ranges, ids


def part1(ranges, ids):
    count = 0
    for i in ids:
        for lo, hi in ranges:
            if i >= lo and i <= hi:
                count += 1
                break
    return count


def part2(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    prev_hi = ranges[0][1]
    count = prev_hi - ranges[0][0] + 1
    for lo, hi in ranges[1:]:
        if hi <= prev_hi:
            continue
        if lo == prev_hi:
            count += hi - lo
            prev_hi = hi
            continue
        if lo > prev_hi:
            count += hi - lo + 1
            prev_hi = hi
            continue
        if lo <= prev_hi and hi > prev_hi:
            count += hi - prev_hi
            prev_hi = hi
            continue
    return count


if __name__ == "__main__":
    ranges, ids = parse(INPUT)
    # print(part1(ranges, ids))
    print(part2(ranges))
