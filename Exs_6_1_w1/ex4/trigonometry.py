import factorial

def calc_sin (x, n):
    temp = 0
    for count_n in range(n):
        temp += ((-1)**count_n) * ( (x**(2*count_n+1)) / (factorial.calc_factorial(2*count_n+1)) )
    return temp

def calc_cos (x, n):
    temp = 0
    for count_n in range(n):
        temp += ((-1)**count_n) * ( (x**(2*count_n)) / (factorial.calc_factorial(2*count_n)) )
    return temp

def calc_sinh (x, n):
    temp = 0
    for count_n in range(n):
        temp +=  (x**(2*count_n+1)) / (factorial.calc_factorial(2*count_n+1)) 
    return temp

def calc_cosh (x, n):
    temp = 0
    for count_n in range(n):
        temp +=  (x**(2*count_n)) / (factorial.calc_factorial(2*count_n)) 
    return temp

