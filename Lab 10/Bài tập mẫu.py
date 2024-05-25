"""
Bài 1:
Viết một module sohoc.py trong đó gồm các phương thức tính toán cơ bản: 
cộng, trừ, nhân, chia, lũy thừa. 
Sau đó viết chương trình tính toán số học dựa trên các hàm được 
viết và lưu trong module sohoc.

from sohoc import *
a,b = map(float, input("Nhập vào hai số a, b: ").split())
phep_cong = cong(a,b)
phep_tru = tru(a,b)
phep_nhan = nhan(a,b)
phep_chia = chia(a,b)
phep_luythua = luythua(a,b)
print("Phép cộng hai số:", phep_cong)
print("Phép trừ hai số:", phep_tru)
print("Phép nhân hai số:", phep_nhan)
print("Phép chia hai số:", phep_chia)
print("Lũy thừa hai số:", phep_luythua)
"""

"""
Bài 2:
Giả sử cho một danh sách A = [[1,2,3], [4,5,6], [7,8,9]]. Thực hiện 
các yêu cầu sau:
2.1. Xây dựng một module đặt tên là MyMatrix chứa các phương thức bổ 
sung cho đối tượng danh sách, trong đó viết các hàm dưới đây:
a) isMatrix(A) kiểm tra lại xem list A có phải là một biểu diễn ma trận 
không? Trả về kết quả True nếu đúng và False nếu sai
b) inMatrix(A), hàm in ma trận A ra màn hình
c) isSquare(A), kiểm tra xem A có là ma trận vuông không?
d) ChangeRow(A,i,j), hàm thay đổi 2 hàng của ma trận A. 
Nếu A không phải là ma trận hoặc không thực hiện được thì trả lại False, 
nêu thực hiện thành công thì trả về True.
e) Change Column(A,i,j), hàm thay đổi 2 cột của ma trận A. 
Nếu A không phải là ma trận hoặc không thực hiện được thì trả lại False, 
nêu thực hiện thành công thì trả về True.
f) Transpose(A), hàm trả lại kết quả là ma trận A^T là ma trận chuyển vị của A.
g) GetSymetry (A), kiểm tra ma trận vuông A có phải là ma trận đổi xứng không 2 Trà về kết quả là True nếu A là ma trận đối xứng và False nếu A không phải là ma thận đối xứng.
2.2. Viết chương trình sử dụng các hàm trong module MyMatrix vừa được xây dựng ở trên để kiểm tra danh sách A có thỏa mãn các điều kiện trong mục 2.1.

import mymatrix
A = [[1,2,3], [4,5,6], [7,8,9]]
if mymatrix.isMatrix(A):
    print("A là một ma trận")
else:
    print("A không phải là ma trận")

mymatrix.inMatrix(A)

if mymatrix.isSquare(A):
    print("A là một ma trận vuông")
else:
    print("A không phải là ma trận vuông")

if mymatrix.ChangeRow(A, 1, 2):
    print("Có thể thay đổi hàng 1 cho hàng 2")
else:
    print("Không thể đổi chỗ 2 hàng")

if mymatrix.ChangeRow(A, 1, 3):
    print("Có thể thay đổi cột 1 cho cột 3")
else:
    print("Không thể đổi chỗ 2 cột")

chuyen_vi = mymatrix.transpose(A)
print("Ma trận chuyển vị \n", chuyen_vi)

if mymatrix.GetSymetry(A):
    print("A là một ma trận đối xứng")
else:
    print("A không phải là ma trận đối xứng")
"""

"""
Bài 3:
Xây dựng một module có tên Tinh_Toán_Matrix.py gồm các phương thức sau:
+ Add Matrix(A,B), hàm trả về tổng của 2 ma trận.
+ Sub Matrix(A.B), hàm trả vệ hiệu của 2 ma trận.
+ Mul Matrix(A,B), hàm trả về tích của 2 ma trận.
Viết chương trình sử dụng module Tình_ Toan Matrix.py.

from mypackage import tinhtoanmatrix as t
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
tong = t.cong_ma_tran(A,B)
if tong == -1:
    print("Không có phép cộng hai ma trận")
else:
    print(tong)

nhan = t.nhan_ma_tran(A,B)
if nhan == -1:
    print("Không có phép nhân hai ma trận")
else:
    print(nhan)
"""

"""
Bài 4:
Cho hình tròn (C) tọa độ tâm là điểm O(x,y) (x, y có thể nhập từ bàn phím)
, bán kinh r (nhập từ bàn phím).
Xây dựng module có tên hinhtron.py gồm có các phương thức như sau:
a) get_ChuVi(r), hàm trả về chu vi hình tròn với r là bán kính.
b) get_DienTich(r), hàm trả về diện tích hình tròn với r là bán kính.
c) is_In(O,A) trả về True nếu A nằm trong hình tròn C, ngược lại trả vè False 
d) is_Out(O,A) trả về True nếu A nằm ngoài hình tròn C, ngược lại trả về False.
e) is_On(O,A) trả về True nếu A nằm trên hình tròn C, ngược lai trả về False.
"""
