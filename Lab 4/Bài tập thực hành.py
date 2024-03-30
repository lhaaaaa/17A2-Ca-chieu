# Bài 1: Tính tổng
'''
n = int(input("Nhập số nguyên từ bàn phím: "))
i = 1
S1 = 0
S2 = 0
S3 = 0
S4 = 0
S5 = 0
S6 = 0
if n <= 0:
    print("Nhập lại số nguyên dương")
else:
    while i <= n:
        S1 = S1 + i**2 
        if i % 2 != 0:
            S2 = S2 + i**3
        else:
            S3 = S3 + i**4
        S4 = S4 + ((-1)**(i - 1))/i
        S5 = S5 + 1/(i*(i + 1))
        if i >= 2:
            S6 = S6 + 1/(i**0.5)
        i += 1
    print("S1 =", S1)
    print("S2 =", S2)
    print("S3 =", S3)
    print("S4 =", S4)
    print("S5 =", S5)
    print("S6 =", S6)
'''

"""
Bài 2:
Viết chương trình nhập vào tử số và mẫu số của một phân số, kiểm tra mẫu số nhập là số 0 thì nhập lại.
"""
'''
tu_so = int(input("Nhập vào tử số: "))
mau_so = int(input("Nhập vào mẫu số: "))

if mau_so == 0:
    print("Yêu cầu nhập lại mẫu số")
else:
    a = tu_so
    b = mau_so
    if a > b:
        while b != 0:
            a, b = b, a % b
        ucln = a
        tu_so_moi = int(tu_so / a)
        mau_so_moi = int(mau_so / a)
        print(f"Phân số {tu_so}/{mau_so} sau khi rút gọn là: {tu_so_moi}/{mau_so_moi}")
    elif a < b:
        while a != 0:
            b, a = a, b % a
        ucln = b
        tu_so_moi = int(tu_so / b)
        mau_so_moi = int(mau_so / b)
        print(f"Phân số {tu_so}/{mau_so} sau khi rút gọn là: {tu_so_moi}/{mau_so_moi}")
    else:
        print("Phân số bằng 1")
'''
"""
Bài 5: Viết chương trình tìm bội chung nhỏ nhất của hai số nguyên được nhập từ bàn phím.
Tìm BCNN thông qua giải thuật Euclide:
+ Tính UCLN của a và b bằng cách sử dụng giải thuật Euclid
+ Sau khi tìm được UCLN(a, b), ta có thể tính BCNN của a và b bằng công thức: 
BCNN(a, b) = (a * b) / UCLN(a, b)
"""
'''
a, b = map(int, input("Nhập vào hai số a và b: ").split())
# Tìm UCLN của 2 số a và b
a_biendoi = a
b_biendoi = b
ucln = 0
if a_biendoi > b_biendoi:
    while b_biendoi != 0:
            a_biendoi, b_biendoi = b_biendoi, a_biendoi % b_biendoi
    ucln = a_biendoi
elif a_biendoi < b_biendoi:
    while a_biendoi != 0:
        b_biendoi, a_biendoi = a_biendoi, b_biendoi % a_biendoi
    ucln = b_biendoi
else:
    ucln = a_biendoi
# Tìm BCNN của 2 số a và b
tich = a * b 
bcnn = tich/ucln
print(f"BCNN của 2 số {a} và {b} là: {int(bcnn)}")
'''
'''
# Bài 4: Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ
n = int(input("Nhập số từ bàn phím: "))
count = 0
a = n 
# Tính số chữ số có trong số được nhập
while True:
    phan_du = a % 10
    count += 1 
    a = a // 10
    if a == 0:
        break
print("Số chữ số của số đã cho là:", count)

# In ra cách đọc từng chữ số
"""
Ví dụ: 123 -> count = 3 
chu_so_thu_i = 123 // 10^2 = 123 // 100 = 1
phan_du_thu_i = 123 % 10^2 = 123 % 100 = 23
"""
print("Cách đọc: ")
for i in range(count, 0, -1):
    chu_so_thu_i = n // 10**(i-1)
    if chu_so_thu_i == 1:
        print("một", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 2:
        print("hai", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 3:
        print("ba", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 4:
        print("bốn", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 5:
        print("năm", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 6:
        print("sáu", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 7:
        print("bảy", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 8:
        print("tám", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 9:
        print("chín", end = " ")
        n = n % 10**(i-1)
    elif chu_so_thu_i == 0:
        print("không", end = " ")
        n = n % 10**(i-1)
'''

"""
Bài 6: Viết chương trình nhập một số và tính tổng các chữ số của số vừa nhập rồi hiển thị kết quả.
"""
n = int(input("Nhập số từ bàn phím: "))
count = 0
a = n 
tong = 0 
# Tính số chữ số có trong số được nhập
while True:
    phan_du = a % 10
    count += 1 
    a = a // 10
    if a == 0:
        break
print("Số chữ số của số đã cho là:", count)

# Tính tổng 
for i in range(count, 0, -1):
    chu_so_thu_i = n // 10**(i-1)
    tong += chu_so_thu_i
    n = n % 10**(i-1)
print("Tổng các số của số đã cho là:", tong)
    
