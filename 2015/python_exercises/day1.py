data = "data.txt"

count = 0
with open(data) as f:
    for i, char in enumerate(f.readline()):
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count == -1:
            print(i + 1)

# print(count)
