##def fibonacci(x):
##    a=1
##    b=1
##    while b <= x:
##        c = b
##        d = a + b
##        a = c
##        b = d
##    return a
##
##def index_fib_z_x_stevkami(x):
##    a = 1
##    while len(str(fibonacci(a))) <= x:
##        a += 1
##    return a

def Fibonacci(x, y, num_digits):
    c = 0
    a = x
    b = y
    count = 2
    while len(str(c)) < num_digits:
        c = a + b
        a = b
        b = c
        count = count + 1
    return count

