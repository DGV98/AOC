INPUT = "./data/day3/data.txt"


def parse(input):
    banks = []
    with open(input) as f:
        for line in f.readlines():
            line = line.strip()
            bank = []
            for char in line:
                bank.append(int(char))
            banks.append(bank)
    return banks
                
def get_max_power(bank):
    max_val = max(bank)
    ind_max = bank.index(max_val)
    n = len(bank)
    if ind_max == n - 1:
        max_val = max(bank[:n-1])
        ind_max = bank.index(max_val)
    second_max = max(bank[ind_max + 1:])
    joltage = str(max_val) + str(second_max)
    return int(joltage)

def part1(banks):
    total = 0
    for bank in banks:
        # print(bank)
        total += get_max_power(bank)
    return total

def get_max_joltage(bank):
    n = len(bank)
    ans = ""
    num = 9 
    i = 0
    while len(ans) < 12:
        prev_i = i
        try:
            i = i + bank[i:].index(num)
            if i <= n - (12 - len(ans)):
                ans += str(num)
                i += 1
                num = 9
            else:
                i = prev_i
                num -= 1
        except:
            i = prev_i 
            num -= 1
    return int(ans)


def part2(banks):
    total = 0
    for bank in banks:
        total += get_max_joltage(bank)
    return total
        


if __name__ == "__main__":
    banks = parse(INPUT)
    print(part2(banks))

