INPUT = "./data/day2/data.txt"

def parse(input_path):
    output = []
    with open(input_path) as f:
        line = f.readline()
        ranges = line.split(",")
        for r in ranges:
            lo, hi = r.split("-")
            output.append((int(lo), int(hi)))
    return output

def is_dupe(number:int):
    number = str(number)
    n = len(number)
    print(f"number: {number}, num: {number[:n//2]} ber: {number[n//2:]}")
    return number[:n//2] == number[n//2:]
                 
def is_invalid(number: int):
    number = str(number)
    n = len(number)
    i = 1
    while i <= (n // 2):
        win = number[:i]
        count = number.count(win)
        if count * i == n:
            return True
        i += 1
    return False

def part1(ranges: list[tuple]):
    total = 0
    for lo, hi in ranges:
        for num in range(lo, hi + 1):
            if is_invalid(num):
                total += num
    return total 


if __name__ == "__main__":
    ranges = parse(INPUT)
    print(part1(ranges))
    # print(is_invalid(11))
    # print(is_invalid(123123123))
    # print(is_invalid(12345))
