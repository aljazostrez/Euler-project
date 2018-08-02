from math import factorial
def sum_of_nums_in_factorial_x(x):
    result = []
    for i in range(0, len(str(factorial(x)))):
        result.append(int(str(factorial(x))[i]))
    return sum(result)
