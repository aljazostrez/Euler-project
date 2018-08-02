def sum_of_self_powers_to_x(x):
    result = 0
    for i in range(1, x + 1):
        result += (i ** i)
    return result

def last_ten(x):
    result = []
    for i in range(1,11):
        result.append(str(sum_of_self_powers_to_x(x))[-11 + i])
    return int(''.join(result))
