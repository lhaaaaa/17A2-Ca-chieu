"""
Bài 1: 
Viết một module my_Triange, chứa các hàm và thủ tục liên quan đến tam giác như sau:
+ is_ TamGiac(a,b,c), hàm kiểm tra xem bộ 3 số a, b, c có tạo thành một tam giác không? Trả lại True nếu đúng và False nếu sai.
+ ChuviTamGiac(a,b,c), hàm tính chu vi tam giác
+ S_ TamGiac (a,b,c), hàm tính diện tích tam giác.
Viết chương trình sử dụng module trên.

import mytriangle
a,b,c = map(float, input("Nhập vào 3 cạnh của tam giác: ").split())
if mytriangle.istamgiac(a,b,c):
    print("Ba số lập thành 3 cạnh của tam giác")
else:
    print("Ba số không lập thành 3 cạnh của tam giác")

chu_vi = mytriangle.chuvi(a,b,c)
if chu_vi == -1:
    print("Ba số không lập thành 3 cạnh của tam giác")
else:
    print("Chu vi tam giác:", chu_vi)

dien_tich = mytriangle.dientich(a,b,c)
if dien_tich == -1:
    print("Ba số không lập thành 3 cạnh của tam giác")
else:
    print("Diện tích tam giác:", dien_tich)
"""

"""
Bài 3: 
Xây dựng một module có tên sohoc2.py gồm các phương thức:
+ Ucln(a,b), trả về ước chung lớn nhất của 2 số nguyên a, b.
+ Bcnn(a,b), trả về bội số chung nhỏ nhất của 2 số nguyên a, b.
+ SumDivisor(n), trả về tổng các ước của n.
Viết chương trình sử dụng module sohoc2.py trên.

import sohoc2
a,b = map(int, input("Nhập vào 2 số a, b: ").split())

uoc_chung_lon_nhat = sohoc2.ucln(a,b)
print("Ước chung lớn nhất của hai số là:", uoc_chung_lon_nhat)

boi_chung_nho_nhat = sohoc2.bcnn(a,b)
print("Bội chung nhỏ nhất của hai số là:", boi_chung_nho_nhat)

tong_uoc_a = sohoc2.sumdivisor(a)
print("Tổng các ước của số a là:", tong_uoc_a)

tong_uoc_b = sohoc2.sumdivisor(b)
print("Tổng các ước của số b là:", tong_uoc_b)
"""

"""
Bài 4: 
Xây dựng module thực hiện các việc sau:
+ Giải phương trình bậc nhất một ẩn.
+ Giải phương trình bậc hai một ẩn
Viết chương trình sử dụng module được xây dựng ở trên.
"""

"""
Bài 7: 
Xây dựng một module thực hiện công việc sau:
+ Sinh ngẫu nhiên một dãy số <=100 số nguyên, hiển thị dãy số đó ra màn hình.
+ Liệt kê và hiển thị các số nguyên tố chia hết cho 7 trong dãy đó.
+ Tính tổng các số lẻ thuộc dãy đó.
+ Kiểm tra trong dãy có các số chính phương không? Nếu có hiển thị ra màn hình, ngược lại, in ra thông báo không có số chính phương trong dãy.
Viết chương trình sử dụng module trên.
"""
import bai7

random_numbers = bai7.sinhngaunhien()
print("100 số ngẫu nhiên từ 1 đến 500 là: ")
print(random_numbers)

print("Các số nguyên tố chia hết cho 7 từ dãy ngẫu nhiên trên là:")
chiacho7 = bai7.chiacho7(random_numbers)
print(chiacho7) 

print("Tổng các số lẻ trong dãy ngẫu nhiên trên là:")
tongle = bai7.tong_le(random_numbers)
print(tongle)

print("Các số chính phương trong dãy ngẫu nhiên trên là:")
daychinhphuong = bai7.day


