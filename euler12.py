from math import sqrt, floor
def delitelji_trian_stevila(sum_1_to_x):
    delitelji = []
    trian_stevilo = sum(range(sum_1_to_x + 1))
    for i in range(1, floor(sqrt(trian_stevilo) + 1)):
        if trian_stevilo % i == 0:
            delitelji.append(i)
            delitelji.append(trian_stevilo / i)
    return set(delitelji)

def prvo_trian_st_z_vec_kot_x_delitelji(x):
    a = 1
    while True:
        if len(delitelji_trian_stevila(a)) >= x:
            return(sum(range(a+1)))
            break
        a += 1
