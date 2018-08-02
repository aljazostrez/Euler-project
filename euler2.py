def Fibonacci(x, y, z):
    c = 0
    a = x
    b = y
    vsota = 2
    while c <= z:
        c = a + b
        if c%2 == 0:
            vsota = vsota + c
        else:
            vsota = vsota + 0
        a = b
        b = c
    return vsota

def vsota_lihih(x, y, z):
    vsota = Fibonacci(x, y, z)
    print (vsota)

Fibonacci(1, 2, 4000000)
