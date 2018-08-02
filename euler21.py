from math import floor, sqrt
import time


def vsota_deliteljev(n):
    delitelji = []
    for i in range(1, int(floor(sqrt(n)))+1):
        if n % i == 0:
            delitelji.append(i)
            delitelji.append(int(n / i))
    return sum(set(delitelji))-n

        
def sum_of_amicable(n, m):
    vsota = 0
    for i in range(n, m):
        for j in range(n, m):
            if vsota_deliteljev(i) == j and vsota_deliteljev(j) == i and i != j:
                vsota += i
    return vsota

def sum_of_amicable_10000():
    start = time.time()
    vsota = 0
    for i in range(1, 10):
        vsota += sum_of_amicable(1000*(i-1), 1000*i + 1)
    end = time.time()
    print(end-start)
    return vsota


# koda je pomanjkljiva. npr. Kaj če sta para v različnih območjih?
