def prastevilo(x):
    if x > 1:
        for i in range (2, x):
            if (x % i) == 0:
                break
        else:
            return (True)
    else:
        return (False)

#def j_to_prastevilo_do_x(j, x):
#    prastevila = []
#    for i in range(2, x + 1):
#        if prastevilo(i) == True:
#            prastevila.append(i)
#    return prastevila[j-1]
prastevila = []
def j_to_prastevilo(x):
    prastevila.clear()
    a = 1
    while len(prastevila) < x:
        if prastevilo(a) == True:
            prastevila.append(a)
            a = a + 1
        else:
            a = a + 1
    return prastevila[x - 1]
