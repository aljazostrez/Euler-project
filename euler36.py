def palindromic_numbers(n=1000000):
    def binarni(x):
        a = bin(x)[2:]
        return a == a[::-1]
    def decimalni(x):
        a = str(x)
        return a == a[::-1]
    seznam = []
    for i in range(1, n):
        if binarni(i) and decimalni(i):
            seznam.append(i)
    return seznam

sum(palindromic_numbers())
