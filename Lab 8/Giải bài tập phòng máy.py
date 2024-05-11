"""
Bài 2: 
a) Viết chương trình tìm ước chung lớn nhất của 2 số a, b.
b) Xây chương trình tìm bội chung nhỏ nhất của 2 số a, b.
c) Viết chương trình cho phép thực hiện rút gọn phân số.
Hướng dẫn:
+ Tìm UCLN của tử số và mẫu số.
+ Chia tử và mẫu của phân số cho UCLN vừa tìm được.

def uoc_chung_lon_nhat(a,b):
    if a <= 0 and b <= 0:
        print("Hai số không hợp lệ")
    else:
        while b!= 0:
            a, b = b, a % b
        return a

def boi_chung_nho_nhat(a,b):
    ucln = uoc_chung_lon_nhat(a,b)
    bcnn = (a*b)//ucln
    return bcnn

def rut_gon_phan_so(a,b):
    ucln = uoc_chung_lon_nhat(a,b)
    tu_so_moi = a // ucln
    mau_so_moi = b // ucln
    return tu_so_moi, mau_so_moi

a, b = map(int, input("Nhập vào 2 số nguyên: ").split())
ucln = uoc_chung_lon_nhat(a, b)
print(f"Ước chung lớn nhất của 2 số {a} và {b} là:", ucln)
bcnn = boi_chung_nho_nhat(a, b)
print(f"Bội chung nhỏ nhất của 2 số {a} và {b} là:", bcnn)
tu_so, mau_so = rut_gon_phan_so(a, b)
print(f"Phân số {a}/{b} rút gọn được {tu_so}/{mau_so}")
"""

"""
Bài 6: 
Viết chương trình nhập Họ tên, điểm Toán, điểm Lý, điểm Hóa của một sinh viên. 
Tính điểm trung bình và xuất ra kết quả.
(Yêu cầu: Viết hàm nhập, xuất, tính trung bình).

def nhap_thong_tin():
    ho_ten = input("Nhập tên sinh viên: ")
    diem_toan, diem_ly, diem_hoa = map(float, input("Nhập điểm sinh viên: ").split(","))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    trung_binh = round((diem_toan + diem_ly + diem_hoa)/3,2)
    return trung_binh

def xuat_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa, trung_binh):
    print("Thông tin của sinh viên:")
    print("Họ tên:", ho_ten)
    print(f"Điểm 3 môn Toán, Lý, Hóa: {diem_toan}, {diem_ly}, {diem_hoa}")
    print("Điểm trung bình 3 môn là:", trung_binh)

def main():
    ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()
    trung_binh = diem_trung_binh(diem_toan, diem_ly, diem_hoa)
    xuat_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa, trung_binh)

if __name__ == "__main__":
    main()
"""


"""
Bài 7: 
Viết chương trình tính lương của nhân viên:
+ Viết hàm nhập họ tên, quê quán, thâm niên công tác của một nhân viên
+ Viết hàm tính lương dựa vào thâm niên công tác.
+ Viết hàm xuất họ tên, quê quán, thâm niên công tác và lương của nhân viên.
+ Viết chương trình nhập thông tin của nhân viên, tính lương và xuất thông tin của nhân viên (kể cả lương) ra màn hình bằng cách sử dụng ba hàm trên.

def nhap_thong_tin():
    ho_ten = input("Nhập thông tin của nhân viên: ")
    que_quan = input("Nhập quên quán của nhân viên: ")
    tham_nien = float(input("Nhập thâm niên của nhân viên: "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 1000
    luong = tham_nien * luong_co_ban
    return luong

def xuat_thong_tin(ho_ten, que_quan, tham_nien, luong):
    print("Thông tin của nhân viên là:")
    print("Họ và tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác (năm):", tham_nien)
    print("Lương nhân viên ($):", luong)

def main():
    ho_ten, que_quan, tham_nien = nhap_thong_tin()
    luong = tinh_luong(tham_nien)
    xuat_thong_tin(ho_ten, que_quan, tham_nien, luong)

if __name__ == "__main__":
    main()
"""

"""
Bài 9: 
Viết chương trình thực hiện các yêu cầu sau:
+ Tạo một list có n phần tử là số nguyên được nhập từ bàn phím.
+ Sử dụng map, lambda: Tạo một list chứa bình phương của các số 
hạng thuộc list trên.

# Cách 1: Không sử dụng hàm
n = int(input("Nhập vào số n: "))
lst1 = []
for i in range(1, n+1):
    a = int(input(f"Nhập phần tử thứ {i}: "))
    lst1.append(a)
print(lst1)
lst1_moi = []
for phan_tu in lst1:
    b = phan_tu ** 2
    lst1_moi.append(b)
print(lst1_moi)

# Cách 2: Sử dụng hàm map, lambda
n = int(input("Nhập vào số n: "))
lst2 = []
for i in range(1, n+1):
    a = int(input(f"Nhập phần tử thứ {i}: "))
    lst2.append(a)
print(lst2)
lst2_moi = list(map(lambda x: x**2, lst2))
print(lst2_moi)
"""

"""
Bài 10:
a) Viết chương trình tạo một list chứa toàn số chẵn thuộc 
khoảng đóng [1,100].
b) Viết chương trình nhập vào một danh sách các số nguyên từ 1 đến n 
(n có thể nhập từ bàn phím), sử dụng filter và reduce để viết 
hàm tính tổng các số chẵn trong danh sách đã nhập.
"""
lst_a = list(filter(lambda x: x%2 == 0, range(1, 101)))
print(lst_a)

n = int(input("Nhập số nguyên từ bàn phím: "))
import functools
lst_b = list(range(1, n + 1))
sum_chan = functools.reduce(lambda x, y: x+y, list(filter(lambda x: x%2 == 0, lst_b)))
print(sum_chan)