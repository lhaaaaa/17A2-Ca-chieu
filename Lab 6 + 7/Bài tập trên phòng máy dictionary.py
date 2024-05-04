"""
Bài 2: 
Thống kê chiều cao của các học sinh trong nhóm sinh viên được kết quả như sau:
161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163
162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170. 
a) Hỏi nhóm có bao nhiêu sinh viên?
b) Tính chiều cao trung bình của các sinh viên trong nhóm.
c) Liệt kê các chiều cao khác nhau sinh viên trong nhóm.

chieu_cao = "161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163 162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170"
chieu_cao_sv = chieu_cao.split()
print("Số sinh viên của nhóm là:", len(chieu_cao_sv))
tong = 0
for chieucao in chieu_cao_sv:
    tong += int(chieucao)
chieu_cao_tb = tong/len(chieu_cao_sv)
print("Chiều cao trung bình của nhóm sinh viên là:", chieu_cao_tb)
dict1 = {}
for i in chieu_cao_sv:
    count = 0
    for j in chieu_cao_sv:
        if i == j:
            count += 1
    dict1[i] = count
print("Danh sách chiều cao và số lượng theo từng chiều cao là:\n", dict1)
"""

"""
Bài 5: 
Viết chương trình nhập 2 số tự nhiên m, n. Tính tổng các chữ số chung của m và n. 
Ví dụ: m = 1123499, n = 112229; có chữ số chung là 1, 2, 9 do đó tổng các chữ số chung bằng 1+2+9 = 12. 
Trường hợp có một chữ số xuất hiện nhiều lần trong cả m và n thì chữ số đó chỉ được tính một lần.

m, n = map(int, input("Nhập vào 2 số tự nhiên: ").split())
chuoi_m = str(m)
chuoi_n = str(n)
dict1 = {}
tong = 0
for i in chuoi_m:
    count = 0
    for j in chuoi_n:
        if i == j:
            count += 1
            dict1[i] = count 
for key in dict1:
    tong += int(key)
print(f"Tổng các chữ số chung của {m} và {n} là {tong}")
"""

"""
Bài 7: 
Với một số nguyên n nhất định (có thể được nhập từ bàn phím), hãy viết chương trình để tạo ra một dictionary chứa (i: i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. 
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4:16, 5: 25, 6: 36, 7: 49, 8: 64}.

n = int(input("Nhập số nguyên n từ bàn phím: "))
if n <= 0:
    print("Nhập lại số nguyên")
else:
    dict1 = {x: x**2 for x in range(n)}
    print(dict1)
"""

"""
Bài 8: 
b) Cho hai danh sách list gồm n số khác nhau [a0,a1,...,an] và danh sách list2 gồm n tên [ten0, ten1,...,tenn]. Viết chương trình tạo ra một từ điển với các phần tử có dạng <ai>:<teni>. In ra màn hình nội dung của từ điển.

list_so = []
list_ten = []
n = int(input("Nhập số n: "))
for i in range(n+1):
    so = int(input("Nhập số từ bàn phím: "))
    list_so.append(so)
print(list_so)
for i in range(n+1):
    ten = input("Nhập tên từ bàn phím: ")
    list_ten.append(ten)
print(list_ten)
dict1 = {}
for i in range(n+1):
    dict1[list_so[i]]= list_ten[i]
print(dict1)
"""

"""
Bài 9: 
Viết chương trình nhập thông tin sinh viên gồm: 
Mã sinh viên (6 ký tự số), tên sinh viên, điểm số 
và lưu thông tin trong một từ điển. 
Điểm số được làm tròn là một số nguyên thuộc {0,1,2,...,10}. 
Thống kê và sắp xếp các sinh viên theo giá trị điểm giảm dần 10, 9,..,1, 0.

dict1 = {}
i = 1 
while True:
    ma_sv = input("Nhập mã sinh viên: ")
    if ma_sv == '0':
        break
    ten_sv = input("Nhập tên sinh viên: ")
    diem_sv = float(input("Nhập điểm sinh viên: "))
    thong_tin = []
    thong_tin.append(ma_sv)
    thong_tin.append(ten_sv)
    thong_tin.append(diem_sv)
    dict1[i] = thong_tin
    i += 1 
print(dict1)
"""

"""
Bài 11:
Tạo một từ điển lưu dữ liệu thông tin nhân viên một công ty với n nhân viên 
(n được nhập từ bàn phím) bao gồm cặp <key>:<value> là Mã nhân viên gồm 
4 ký tự là chữ số 0,1,2,...9. Họ tên nhân viên (gồm 20 ký tự), năm sinh, lương. 
Thực hiện các yêu cầu sau:
a) Tạo mới từ điển.
b) Thêm nhân viên với các thông tin được nhập từ bàn phím.
c) Tìm kiếm nhân viên với giá trị mã nhân viên là x, với x nhập từ bàn phím.
d) Tăng lương 1000 cho nhân viên có mã là y, trong từ điển.
e) Xóa nhân viên có mã là z, z nhập từ bàn phím.
f) Sắp xếp từ điển giảm dần theo năm sinh.

n = int(input("Nhập số lượng nhân viên: "))
dict1 = {}
i = 1 
while i < n + 1:
    thong_tin_nhan_vien = []
    ma_nhanvien = input("Nhập mã nhân viên: ")
    ho_ten = input("Nhập họ tên nhân viên: ")
    thong_tin_nhan_vien.append(ho_ten)
    nam_sinh = input("Nhập năm sinh của nhân viên: ")
    thong_tin_nhan_vien.append(nam_sinh)
    luong = int(input("Nhập lương của nhân viên: "))
    thong_tin_nhan_vien.append(luong)
    dict1[ma_nhanvien] = thong_tin_nhan_vien
    i += 1

#Tìm kiếm nhân viên
x = input("Nhập mã nhân viên cần tìm: ")
if x in dict1:
    print("Thông tin của nhân viên cần tìm là: ", dict1[x][0], dict1[x][1], dict1[x][2])
else:
    print("Không có thông tin về nhân viên")

#Tăng lương nhân viên
y = input("Nhập mã nhân viên cần tìm: ")
if y in dict1:
    dict1[y][-1] = dict1[y][-1] + 1000
    print("Lương của nhân viên sau khi được tăng là:", dict1[y][-1])
else:
    print("Không có thông tin về nhân viên")

# Xóa nhân viên 
z = input("Nhập mã nhân viên cần tìm: ")
if z in dict1:
    dict1.pop(z)
    print("Thông tin của các nhân viên còn lại là:", dict1)
else:
    print("Không có thông tin về nhân viên")
"""

"""
Bài 6: 
Thi Olympic: Giả sử một trường có n sinh viên tham gia thi Olympic Tin học 
với các ngôn ngữ lập trình C++, Java và Python. Các sinh viên được đánh số 
từ 1 đến n.
+ Ngôn ngữ C++ có a sinh viên dự thi, gồm các sinh vi(ên có số 
thứ tự: t1, t2,.., tn.
+ Ngôn ngữ Java có b sinh viên dự thi, gồm các sinh viên có số 
thứ tự : k1, k2,..., kn.
+ Ngôn ngữ Python có c sinh viên dự thi gồm các sinh viên có số 
thứ tự: h1, h2,...., hn.
Viết chương trình đưa ra danh sách các sinh viên chỉ thi một ngôn ngữ 
lập trình; các sinh viên thi trên 2 ngôn ngữ lập trình và các sinh viên 
dự thi cả 3 ngôn ngữ.
"""
import random
n = int(input("Nhập số lượng sinh viên: "))
a = int(input("Nhập số sinh viên dự thi ngôn ngữ C++: "))
b = int(input("Nhập số sinh viên dự thi ngôn ngữ Java: "))
c = int(input("Nhập số sinh viên dự thi ngôn ngữ Python: "))
danh_sach_a = []
danh_sach_b = []
danh_sach_c = []
if a > n or b > n or c > n:
    print("Số sinh viên dự thi không thỏa mãn")
else:
    for i in range(1, a):
        t = random.randint(1,n)
        danh_sach_a.append(t)
    for j in range(1, b):
        k = random.randint(1,n)
        danh_sach_b.append(k) 
    for z in range(1, c):
        h = random.randint(1,n)
        danh_sach_c.append(h)
print(danh_sach_a)
print(danh_sach_b)
print(danh_sach_c)
danh_sach = {}
for sv in danh_sach_a:
    if sv in danh_sach_b and sv in danh_sach_c:
        danh_sach[sv] = 3
    elif sv in danh_sach_b and sv not in danh_sach_c:
        danh_sach[sv] = 2
    elif sv not in danh_sach_b and sv in danh_sach_c:
        danh_sach[sv] = 2
    elif sv not in danh_sach_b and sv not in danh_sach_c: 
        danh_sach[sv] = 1
print(danh_sach)
thi_1_mon = []
thi_2_mon = []
thi_3_mon = []
for sv in danh_sach:
    if danh_sach[sv] == 1:
        thi_1_mon.append(sv)
    elif danh_sach[sv] == 2:
        thi_2_mon.append(sv)
    elif danh_sach[sv] == 3:
        thi_3_mon.append(sv)
print("Danh sách sinh viên thi 1 môn là:", thi_1_mon)
print("Danh sách sinh viên thi 2 môn là:", thi_2_mon)
print("Danh sách sinh viên thi 3 môn là:", thi_3_mon)