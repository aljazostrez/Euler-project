list = []
for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        if str(z) == str(z)[::-1]:
            list.append(z)

print(max(list))
