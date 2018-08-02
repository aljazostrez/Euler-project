def vsota_stevk_stevila_2_na_x(x):
    rezultat = 0
    for i in range(0, len(str(2 ** x))):
        rezultat += int(str(2 ** x)[i])
    return rezultat
