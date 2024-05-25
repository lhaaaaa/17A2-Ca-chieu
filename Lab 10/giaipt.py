def bac1(a,b):
    if a == 0 and b == 0:
        return "vô số nghiệm"
    elif a == 0 and b!= 0:
        return "vô nghiệm"
    else:
        x = -b/a
        return x
    
def bac2(a,b,c):
    if a == 0:
        bac1(b,c)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "vô nghiệm"
        elif delta == 0:
            x = -b /2*a
            return x
        else:
            x1 = (-b + delta**0.5)/2
            x2 = (-b - delta**0.5)/2
            return x1, x2