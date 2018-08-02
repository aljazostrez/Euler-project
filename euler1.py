def sum_mul_3_5(x):
    rez = 0
    for i in range(x):
        if i%3==0 or i%5==0:
            rez += i
    return rez



