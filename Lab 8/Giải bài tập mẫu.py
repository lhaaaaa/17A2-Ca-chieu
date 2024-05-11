"""
Bài 1:
Xây dựng hàm không tham số tính lũy thừa một số tự nhiên?

def tinh_luy_thua():
    a = int(input("Nhập số từ bàn phím: "))
    luy_thua = a**2 
    return luy_thua

luy_thua = tinh_luy_thua()
print(luy_thua)
"""

"""
Bài 2:
Biết rằng dãy số Fibonacci là dãy số vô hạn, được bắt đầu bởi số 0 và số 1, các số tiếp theo luôn bằng tổng của 1 số liền trước cộng lại
Ví dụ: 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
Viết hàm tìm và in ra màn hình dãy Fibonacci không quá n số hạng (Hàm không có giá trị trả về)

n = int(input("Nhập số từ bàn phím: "))
def day_fib(n):
    if n <= 1:
        print("Dãy fibonacci là: 0, 1")
    else:
        i = 0
        print(0, 1, end = " ")
        a = 0
        b = 1
        while i <= n-3:
            a, b = b, a + b
            print(b, end = " ")
            i += 1
day_fib(n)
"""

"""
Bài 3:
a) Viết chương trình (yêu cầu xây dựng hàm) để nhập số nguyên dương n. Kiểm tra n có phải là số nguyên tố không?
b) Viết chương trình, trong đó xây dưng hàm nhập số nguyên dương n. Kiểm tra n có phải là số hoàn hảo không?
c) Trong toán học số nguyên n gọi là số đối xứng nếu đọc từ trái qua phải, hay từ phải qua trái đều được số giống nhau. Ví dụ: 11, 121, 101 là các số đối xứng.
Viết chương trình (yêu cầu xây dựng hàm) in ra màn hình các số đối xứng trong phạm vị 1000. 
Quy cách in mỗi số đối xứng chiếm 05 ký tự và tối đa 15 số trên một hàng mới chuyển qua hàng mới.

# Kiểm tra số nguyên tố
n = int(input("Nhập số từ bàn phím: "))

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    else: 
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")

# Kiểm tra số hoàn hảo
def tap_uoc(n):
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    return uoc
def kiem_tra_so_hoan_hao(n):
    if n < 0:
        return False
    else:
        sum = 0
        uoc = tap_uoc(n)
        for so in uoc:
            sum += so
        if sum == n:
            return True
        else:
            return False

n = int(input("Nhập số từ bàn phím: "))
if kiem_tra_so_hoan_hao(n):
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không là số hoàn hảo")

def kiem_tra_so_doi_xung(n):
    if n < 0:
        return False
    else:
        chuoi_so = str(n)
        so_dao_nguoc = chuoi_so[::-1]
        if chuoi_so == so_dao_nguoc:
            return True
        else:
            return False
for i in range(10, 1000):
    if kiem_tra_so_doi_xung(i):
        print(i, end = " ")
"""

"""
Bài 4:
a) Viết chương trình (yêu cầu xây dựng hàm) tính P(n) = 1 x 3 x 5 x … x (2n+1) (n >=0)
b) Viết chương trình (yêu cầu xây dựng hàm) để tính: S(n) = 1 - 2 + 3 - 4 + 5 - ...+((-1)^(n+1))*n(n>=0).
c) Viết chương trình (yêu cầu xây dựng hàm) để tính: S(n)= 1 + (1+2) + (1+2+3) + ... + (1+2+3+..+n).
d) Viết chương trình (yêu cầu xây dựng hàm) để tính:  P(x,y) = x^y

def tich_cau_a(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich

def tong_cau_b(n):
    if n < 0:
        return 0
    else:
        sum = 0
        for i in range(1, n+1):
            sum += ((-1)**(n+1))*n
        return sum

def tong_cau_c(n):
    if n < 0:
        return 0
    else:
        sum = 0
        for i in range(1, n+1):
            sum2 = 0
            for j in range(1, i+1):
                sum2 += j
            sum += sum2
        return sum
    
n = int(input("Nhập số nguyên từ bàn phím: "))
tich_a = tich_cau_a(n)
print("Kết quả câu a là:", tich_a)
tong_b = tong_cau_b(n)
print("Kết quả câu b là:", tong_b)
tong_c = tong_cau_c(n)
print("Kết quả câu c là:", tong_c)

def P(x,y):
    gia_tri = x**y
    return gia_tri

x, y = map(int, input("Nhập 2 số từ bàn phím: ").split())
gia_tri = P(x,y)
print(f"Giá trị của P(x,y) = x^y là {gia_tri}")
"""