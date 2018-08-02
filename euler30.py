def digit_n_powers(n):
    digits = []
    na_n = []
    for a in range(2, n*(10**(n))):
        na_n.clear()
        for i in range(0,len(str(a))):
            na_n.append(int(str(a)[i])**n)
        if sum(na_n) == a:
            digits.append(a)
    return set(digits)

def sum_digit_n_powers(n):
    return sum(digit_n_powers(n))
