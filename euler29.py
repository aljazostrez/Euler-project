def num_of_distinct_terms(a, b, c, d):
    '''izracuna koliko stevil tipa x ^ y, a <= x <= b, c <= y <= d'''
    vsi = []
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            vsi.append(i ** j)
    return len(set(vsi))
