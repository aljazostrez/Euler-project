def vsota_prastevil_do_x(x):
    prastevila = []
    for i in range(0, x+1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
                else:
                    prastevila.append(i)
    return sum(set(prastevila))
