"""  
123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
"""
import re

INPUT = 'data/day6/sample.txt'


def parse(path):
    nums = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            nums.append(re.split("\s+", line))
    operands = nums.pop(-1)
    return nums, operands


def part1(nums, operands):
    n = len(operands)
    i = 0
    sum_results = 0
    while i < n:
        op = operands[i]
        if op == "*":
            total = 1
        else:
            total = 0
        for row in nums:
            if op == "*":
                total *= int(row[i])
            else:
                total += int(row[i])
        print(total)
        sum_results += total
        i += 1
    return sum_results


def parse2(path):
    nums = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            nums.append(line.split(" "))
    operands = nums.pop(-1)
    for i, op in enumerate(operands):
        operands[i] = op.strip()
    return nums, operands


if __name__ == "__main__":
    # nums, operands = parse(INPUT)
    # print(part1(nums, operands))
    print(parse2(INPUT))
