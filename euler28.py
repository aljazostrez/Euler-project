def sum_of_spiral_diagonals_n_x_n(n):
    result = [1]
    step = 2
    a = 1
    while a+step <= n*n:
        for i in range(1,5):
            result.append(a + (step*i))
        a += step*4
        step += 2
    return sum(result)
