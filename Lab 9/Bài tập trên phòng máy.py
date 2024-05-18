"""
Bài 1: 
Viết chương trình nhập 3 số từ bản phím. 
Sử dụng hàm đệ quy tìm số lớn nhất trong ba số.

a,b,c = map(int, input("Nhập 3 số từ bàn phím: ").split())
lst = [a,b,c]
def tim_so_lon_nhat(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], tim_so_lon_nhat(lst[1:]))
print(tim_so_lon_nhat(lst))
"""

"""
Bài 2: 
Sử dụng kỹ thuật đệ qui để viết chương trình nhập n số từ bản phím. 
Tính ước chung lớn nhất của n số đó.

def ucln_2_so(a,b):
    if b == 0:
        return a
    else:
        return ucln_2_so(b, a%b)
    
def ucln_n_so(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return ucln_2_so(lst[0], ucln_n_so(lst[1:]))

n = int(input("Nhập số lượng số nguyên: "))
lstA = []
for i in range(n):
    a = int(input("Nhập số nguyên: "))
    lstA.append(a)
print(lstA)
print("Ước chung lớn nhất của các số là:", ucln_n_so(lstA))
"""

"""
Bài 3: 
Viết chương trình nhập một số a, n từ bàn phím. 
Sử dụng hàm đệ qui tính lũy thừa a^n.

n = int(input("Nhập số mũ: "))
a = int(input("Nhập cơ số: "))
def tinh_luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * tinh_luy_thua(a,n-1)
ket_qua = tinh_luy_thua(a,n)
print(f"Giá trị của {a}^{n} là:", ket_qua)
""" 

"""
Bài 9: 
Tính giai thừa kép:
Biết rằng: Giai thừa kép ký hiệu là n!! được định nghĩa như sau:
n!! = 1, quy ước nếu n = 0 hoặc n = 1
(n - 2)!!n, quy ước nếu n >=2
Tính n!! Sau đó dùng hàm này để tính tổng
S = 1!! - 2!! + …. + (-1)^(k+1)k!! Với k < 1000

def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua_kep(n-2)
k = 1
tong = 0
while k < 50:
    tong += (-1)**(k+1)*giai_thua_kep(k)
    k += 1
print("Tổng các số là:", tong)
"""

"""
Bài 10:
Có bài toán cổ như sau:
"Vừa gà vừa chó
Bó lại cho tròn
Ba mươi sáu con
Một trăm chân chẵn“
Hỏi có bao nhiêu con gà và bao nhiêu con chó?
Hãy viết chương trình dùng kỹ thuật đệ qui giải bài toán trên?

def cho_ga(tong_so_con, tong_so_chan):
    if tong_so_con == 0 and tong_so_chan == 0:
        return 0, 0
    if tong_so_chan % 2 != 0:
        return -1, -1
    for cho in range(tong_so_con + 1):
        ga = tong_so_con - cho
        if ga * 2 + cho * 4 == tong_so_chan:
            return cho, ga
    cho, ga = cho_ga(tong_so_con -1, tong_so_chan -4)
    if ga != -1:
        return cho + 1, ga
    else:
        return -1, -1

tong_so_chan = 120
tong_so_con = 44
so_cho, so_ga = cho_ga(tong_so_con, tong_so_chan)
print("Số gà là:", so_ga)
print("Số chó là:", so_cho)
"""

"""
Bài 7: 
Viết các hàm tính toán sử dụng kỹ thuật đệ qui
"""
def tong_S1(n):
    if n == 0:
        return 0
    else:
        return 1/(n*(n+1)) + tong_S1(n-1)

def tinh_giai_thua(n):
    if n == 1:
        return 1
    else:
        return n*tinh_giai_thua(n-1)

def tong_S2(n):
    if n == 1:
        return 1
    else:
        return 1/tinh_giai_thua(n) + tong_S2(n-1)

def tong_S3(n):
    if n == 1:
        return 3**0.5
    else:
        return (3*n + tong_S3(n-1))**0.5

n = int(input("Nhập số từ bàn phím: "))
S1 = tong_S1(n)
S2 = tong_S2(n)
S3 = tong_S3(n)
print("Tổng S1:", S1)
print("Tổng S2:", S2)
print("Tổng S3:", S3)