def istamgiac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def chuvi(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        return p
    return -1

def dientich(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s
    return -1