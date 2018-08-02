def fakulteta(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fakulteta(n - 1)

digit_factorials = []
for i in range(100000):
    vsota = 0
    for j in range(len(str(i))):
        vsota += fakulteta(int(str(i)[j]))
    if vsota == i:
        digit_factorials.append(i)
print(digit_factorials)
print(sum(digit_factorials)-3)
