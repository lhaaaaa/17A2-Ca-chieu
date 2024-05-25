def ucln(a,b):
    while b !=0:
        a, b = b, a % b
    return a

def bcnn(a,b):
    uoc_chung_lon_nhat = ucln(a,b)
    boi_chung_nho_nhat = (a*b)//uoc_chung_lon_nhat
    return boi_chung_nho_nhat

def sumdivisor(a):
    sum = 0
    for i in range(1, a + 1):
        if a % i == 0:
            sum += i
    return sum