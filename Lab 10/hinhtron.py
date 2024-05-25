def chuvi(r):
    return 2*r*3.14

def dientich(r):
    return r*r*3.14

def vitri(x_o, y_o, x_a, y_a, r):
    x_oa = x_a - x_o
    y_oa = y_a - y_o
    OA = round((x_oa**2 + y_oa**2)**0.5, 2)
    if OA == r:
        return 0
    elif OA > r:
        return 1
    else:
        return 2