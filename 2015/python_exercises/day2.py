data = "data.txt"

total = 0
with open(data) as f:
    for line in f.readlines():
        l, w, h = map(int, line.strip().split("x"))
        total += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)

print(total)

total = 0
with open(data) as f:
    for line in f.readlines():
        l, w, h = map(int, line.strip().split("x"))
        total += min(2 * (l + w), 2 * (w + h), 2 * (l + h)) + (l * w * h)

print(total)
