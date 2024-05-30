def sinhngaunhien():
    import random
    random_numbers = [random.randint(1, 500) for _ in range(100)]
    return random_numbers

def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    else:
        for i in range(2, so):
            if so % i == 0:
                return False
        return True

def chia_het_7(random_numbers):
    lst = []
    for so in random_numbers:
        if kiem_tra_so_nguyen_to(so):
            if so % 7 == 0:
                lst.append(so)
    return lst

def tong_le(random_numbers):
    sum = 0
    for so in random_numbers:
        if so % 2 != 0:
            sum += so
    return sum

def kiem_tra_so_chinh_phuong(so):
    if so**2 == (int(so**0.5))**2:
        return True
    else:
        return False
    
def day_chinh_phuong(random_numbers):
    lst = []
    for so in random_numbers:
        if kiem_tra_so_chinh_phuong(so):
            lst.append(so)
    return lst
