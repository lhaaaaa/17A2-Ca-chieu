"""
Bài 1:
Biết rằng: Trong toán học, một cấp số nhân (geometrie sequence) là một dãy số thoả mãn điều kiện kể từ số hạng thứ hai, mỗi số hạng đều là tích của số hạng đúng ngạy thước nó với một số không đổi. 
Hằng số này được gọi là công bội của cấp số nhân. 
Viết chương trình trong đó áp dụng kỹ thuật đệ qui để xây dựng 
hàm cap _so_ nhan (n) có chức năng tìm được số hạng thứ n 
(n nhập từ bàn phím) của một cấp số nhân với số hạng đầu bằng 7 
và công bội bằng 2.

def cap_so_nhan(n):
    if n == 0:
        return 7
    else:
        return 2*cap_so_nhan(n-1)
n = int(input("Nhập thứ tự của số hạng: "))
ket_qua = cap_so_nhan(n)
print(ket_qua)
"""

"""
Bài 3:
Viết hàm đếm thời gian từ 1 trở đi, mỗi lần đếm là 1 giây. 
Đồng hồ thời gian sẽ dừng lại sau đúng n phút (tức sau n * 60 giây).

def dem_thoi_gian(n):
    if n == 0:
        return 0
    else:
        return 1 + dem_thoi_gian(n - 1)
n = int(input("Nhập vào số phút: "))
n_giay = n * 60
stop = dem_thoi_gian(n_giay)
print("Số giây của thời gian là:", stop)
"""

"""
Bài 4:
Viết một chương trình thực hiện các nội dung sau:
a) Viết một hàm tạo một listA chứa các phần tử là 
n số nguyên được (n) được nhập từ bàn phím.
b) Xây dựng một hàm đệ quy insert(k,x) để chèn số x 
(x được nhập từ bàn phím) vào listA tại vị trí k.

n = int(input("Nhập số nguyên n: "))
def tao_list(n):
    lst = []
    for i in range(n):
        a = int(input("Nhập số nguyên từ bàn phím: "))
        lst.append(a)
    return lst 
lstA = tao_list(n)
print(lstA)
x = int(input("Nhập số cần chèn: "))
k = int(input("Nhập vị trí cần chèn: "))
def chen_phan_tu(lstA, k, x):
    if k == 0:
        return [x] + lstA
    else:
        return [lstA[0]] + chen_phan_tu(lstA[1:], k-1, x)
ket_qua = chen_phan_tu(lstA, k, x)
print(ket_qua)
"""

"""
Bài 5:
Cho trước số tự nhiên n nhập từ bàn phím. 
Viết chương trình sử dụng thuật toán đệ qui để tìm tất cả các khai 
triển N = x1 + x2 +...+ Xk, với xi là số tự nhiên. 
Chương trình cần liệt kê tất cả các bộ nghiệm (x1, x2,.., xk).

n = int(input("Nhập số tự nhiên: "))
def tim_nghiem(n, tong_ban_dau = 0, lst_nghiem = [], tap_lst_nghiem = []):
    if n == tong_ban_dau:
        tap_lst_nghiem.append(lst_nghiem[:])
        return 
    if tong_ban_dau > n:
        return 
    else:
        for i in range(1, n - tong_ban_dau + 1):
            lst_nghiem.append(i)
            tim_nghiem(n, tong_ban_dau + i, lst_nghiem, tap_lst_nghiem)
            lst_nghiem.pop()
    return tap_lst_nghiem 
    
tap_nghiem = tim_nghiem(n)
print(tap_nghiem)
"""

"""
Bài 6:
Tính các tổng sau, sử dụng thuật toán đệ qui để xây dựng hàm
a) S1 = 1 + 2 + 3 +... + n.
b) S2 = 2 + 4 + ...+ 2n.
c) S3 = 1 + 3 + 5 +...+ 2n-1.

n = int(input("Nhập số từ bàn phím: "))
def tong1(n):
    if n == 1:
        return 1
    else:
        return n + tong1(n-1)
ket_qua1 = tong1(n)
print(ket_qua1)

def tong2(n):
    if n == 1:
        return 2
    else: 
        return 2*n + tong2(n-1)
ket_qua2 = tong2(n)
print(ket_qua2)

def tong3(n):
    if n == 1:
        return 1
    else:
        return 2*n - 1 + tong3(n-1)
ket_qua3 = tong3(n)
print(ket_qua3)
"""

"""
Bài 9: 
Bài toán tháp Hà Nội
Có 3 chiếc cột được đánh số A, B, C. Ban đầu cột A có n chiếc đĩa (có lỗ tròn ở giữa), 
n đĩa được đánh số thứ tự từ 1 đến n (Từ trên xuống dưới), đĩa ở trên luôn có đường kính nhỏ hơn đĩa ở bên dưới.
Yêu cầu: Hãy chuyển n đĩa từ cột A sang cột B.
Qui tắc chuyển: Được sử dụng thêm cột C là trung gian
Bước 1: Tại một thời điểm, chi một đĩa được phép di chuyển.
Bước 2: Chỉ đĩa trên cùng mới được phép di chuyển.
Bước 3: Trong quá trình chuyên không được phép đặt đĩa lớn hơm lên trên đĩa nhớ hơn.
"""
def thap_ha_noi(n, A, C, B):
    if n == 1:
        print(f"Chuyển đĩa 1 từ cột {A} sang cột {B}")
    else:
        thap_ha_noi(n-1, A, B, C)
        print(f"Chuyển đĩa {n} từ cột {A} sang cột {B}")
        thap_ha_noi(n-1, C, A, B)

# Chuyển 3 đĩa từ cọc A sang cọc B, với trung gian là cọc C
thap_ha_noi(3, "A", "C", "B")