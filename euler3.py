def prastevilo(x):
    if x > 1:
        for i in range (2, x):
            if (x % i) == 0:
                break
        else:
            return (True)
    else:
        return (False)
        
def prime_factors(x):
    for i in range(2, x):
        if (x % i == 0) and (prastevilo(i) == True):
            print (i, "je praštevilo števila", x)
