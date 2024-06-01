"""
Bài 1:
Viết chương trình nhập dữ liệu từ tập tin text file f_in.txt 
và lưu vào một danh sách, in nội dung của danh sách đó ra màn hình.
Biết file text có dạng như sau:
+ Dòng đầu tiên là số tự nhiên n.
+ Dòng thứ hai là n số được viết cách nhau bởi dấu cách.

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/f_in.txt", "r") as bai1:
    n = bai1.readline()
    so = bai1.readline()
# Chuyển đổi chuỗi thành danh sách số nguyên
data = []
for num in so.split():
    num = int(num)
    data.append(num)
print(data)
"""

"""
Bài 2:
Viết chương trình xây dựng các hàm thực hiện công việc sau:
+ Đọc dữ liệu từ tập tin dạng text fin.dat và chuyển dữ liệu vào tập tin văn bản fount.dat.
+ Biết rằng tập tin fin.dat có dạng:
- Dòng đầu tiên là một số tự nhiên n.
- n dòng tiếp theo, mỗi dòng là một dãy các số nguyên hoặc thực, cách nhau bởi dấu cách. Số lượng các phần tử của mỗi dãy có thể không bằng nhau.
+ Tệp fout.dat có cấu trúc như sau:
- Dòng đầu tiên ghi số S là tổng của tất cả các số trong dãy từ tệp fin.dat.
- n dòng tiếp theo, dòng thứ i ghi số Si là tổng các số của dãy số tương ứng từ tệp fin.dat.


with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/fin.dat.txt", "r") as bai2a:
    lines = bai2a.readlines()
# Chuyển đổi chuỗi số thành số nguyên
day_so = []
for lst in lines[1:]:
    data = []
    for num_str in lst.split():
        num = int(num_str)
        data.append(num)
    day_so.append(data)
print(day_so)
# Tính tổng tất cả các số trong list và tính tổng của tất cả các số trong list con
tong = 0
lst_sum = []
for lst in day_so:
    sum = 0
    for num in lst:
        sum += num
    lst_sum.append(sum)
    tong += sum
print(lst_sum)
print(tong)
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/fount.dat", "w") as bai2b:
    bai2b.write(str(tong) + "\n")
    for sum in lst_sum:
        bai2b.write(str(sum) + "\n")
"""

"""
Bài 3:
Cho trước tập tin văn bản Data.dat có dạng n dòng, mỗi dòng là 1 số. 
Yêu cầu viết hàm đọc dữ liệu từ tập tin Data.dat và chuyển vào dãy list A 
bao gồm n phần tử đọc từ tập tin này sau đó in kết quả ra màn hình.

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/Data.dat.txt", "r") as bai3:
    lines = bai3.read().strip()
# Chuyển chuỗi thành số nguyên và đưa vào list A
A = []
for num in lines.split():
    num = int(num)
    A.append(num)
print(A)
"""

"""
Bài 4:
Cho trước danh sách (listA) bao gồm các số bất kỳ. Viết chương trình ghi ra tập tin văn bản có tên là 'Dulieu.dat' có định dạng là nhiều dòng, các dòng là các số lấy từ A.
Ví dụ: Nếu danh sách A= [0, 0.3, 5.8, 12, 15]
Thì tập tin Dulieu.dat sẽ có dạng:
0
0.3
5.8
12
15

A = [0, 0.3, 5.8, 12, 15]
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/Dulieu.dat", "w") as bai4:
    for num in A:
        bai4.write(str(num) + "\n")
"""

"""
Bài 5:
Cho trước ma trận A dạng mxn (m hàng, n cột) được mô tả theo danh sách như sau:
A=|[a11, a12,..,a1n], [a21, a22,…,a2n],…,[am1,am2,...,2mn]].
Viết chương trình ghi dữ liệu ma trận A ra tập tin văn bản có dạng sau:
+ Dòng đầu tiên ghi 2 số m, n cách nhau bởi dấu cách
+ m dòng tiếp theo, mỗi hàng ghi dãy các số của hàng tương ứng của ma trận A, các số cách nhau bởi dấu phẩy

A = []
m, n = map(int, input("Nhập số hàng và số cột của ma trận A: ").split())
for i in range(m):
    row = []
    for j in range(n):
        phantu = int(input(f"Nhập phần tử hàng {i} cột {j}: "))
        row.append(phantu)
    A.append(row)
print(A)

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/matran.txt", "w") as bai5: 
    bai5.write(str(m) + " " + str(n) + "\n")
    for row in A:
        for phantu in row:
            bai5.write(str(phantu) + " ")
        bai5.write("\n")
"""

"""
Bài 6:
Thực hiện ngược lại bài tập 5. Viết chương trình đọc dữ liệu 
từ tệp văn bản trên vào chuyển vào dãy list A có dạng:
A = [[a11, a12,...,a1n], [a21, a22, ..,a2n],...,[am1,am2,..,2mn]].

# Đọc dữ liệu từ file
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/matran.txt", "r") as bai6:
    lines = bai6.readlines()

# Lấy số hàng và số cột của ma trận từ dòng đầu tiên
m, n = map(int, lines[0].strip().split())

# Chuyển đổi các dòng thành ma trận
A = []
for line in lines[1:]:
    row = [int(x) for x in line.strip().split()]
    A.append(row)

print(f"Ma trận với {m} hàng {n} cột là:")
print(A)
"""

"""
Bài 8: 
Giả sử thông tin sinh viên của một lớp gồm các trường sau:  
Mã sinh viên, Tên sinh viên, Giới tính, Năm sinh. 
Viết chương trình lưu thông tin sinh viên vào một file .CSV 
có tên là sinhvien.csv.

import csv
# Nhập thông tin sinh viên từ bàn phím
data = []
n = int(input("Nhập số sinh viên: "))
print("-----------------")
# Nhập thông tin của từng sinh viên
for i in range(1, n+1):
    sv = {}
    sv["Mã sinh viên"] = input(f"Nhập mã sinh viên của sinh viên thứ {i}: ")
    sv["Tên sinh viên"] = input(f"Nhập tên sinh viên thứ {i}: ")
    sv["Giới tính"] = input(f"Nhập giới tính của sinh viên thứ {i}: ")
    sv["Năm sinh"] = input(f"Nhập năm sinh của sinh viên thứ {i}: ")
    print("----------------")
    data.append(sv)

# Ghi dữ liệu vào file csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/sinhvien.csv", "w", encoding= "utf-8") as bai8:
    fieldnames = ["Mã sinh viên", "Tên sinh viên", "Giới tính", "Năm sinh"]
    write = csv.DictWriter(bai8, fieldnames= fieldnames)
    write.writeheader()
    for sv in data:
        write.writerow(sv)
"""

"""
Bài 9: 
Giả sử có file sinhvien.csv với nội dung như ở bài trên. Viết chương trình thực hiện các yêu cầu sau:
a) Đọc thông tin sinh viên từ file sinhvien.csv, in dữ liệu các sinh viên ra màn hình.
b) Sắp xếp sinh viên theo thứ tự giảm dần của năm sinh. In ra kết quả trước và sau khi sắp xếp.
c) Thêm một sinh viên mới với đây đủ thông tin được nhập từ bàn phím mà không làm ảnh hưởng kết quả sắp xếp.
d) Tìm kiếm sinh viên có mã số x, với x được nhập từ bàn phím.
e) Xóa sinh viên có năm sinh là y, với y được nhập từ bàn phím.
"""
import csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/sinhvien.csv", "r", encoding= "utf-8") as bai9:
    read = csv.DictReader(bai9)
    data = list(read)
# In dữ liệu của sinh viên
print("Thông tin sinh viên:")
for sv in data:
    print(f'Mã sinh viên: {sv["Mã sinh viên"]}')
    print(f'Tên sinh viên: {sv["Tên sinh viên"]}')
    print(f'Giới tính: {sv["Giới tính"]}')
    print(f'Năm sinh: {sv["Năm sinh"]}')
    print("---------------------")

# Sắp xếp sinh viên theo thứ tự giảm dần của năm sinh
data.sort(key = lambda x: int(x["Năm sinh"]))

# In ra kết quả sau khi sắp xếp
print("Kết quả sau khi sắp xếp theo năm sinh là: ")
for sv in data:
    print(f'Mã sinh viên: {sv["Mã sinh viên"]}')
    print(f'Tên sinh viên: {sv["Tên sinh viên"]}')
    print(f'Giới tính: {sv["Giới tính"]}')
    print(f'Năm sinh: {sv["Năm sinh"]}')
    print("---------------------")

# Tìm kiếm sinh viên có mã số x, với x được nhập từ bàn phím.
maso = input("Nhập mã số cần tìm: ")
for sv in data:
    if sv["Mã sinh viên"] == maso:
        print("Có thông tin sinh viên: ")
        print(f'Mã sinh viên: {sv["Mã sinh viên"]}')
        print(f'Tên sinh viên: {sv["Tên sinh viên"]}')
        print(f'Giới tính: {sv["Giới tính"]}')
        print(f'Năm sinh: {sv["Năm sinh"]}')
        break
    else:
        print("Không tìm thấy thông tin sinh viên")

# Xóa sinh viên có năm sinh là y, với y được nhập từ bàn phím.
namsinh = input("Nhập năm sinh cần tìm: ")
for sv in data:
    if sv["Năm sinh"] == namsinh:
        data.remove(sv)
        print("Đã xóa sinh viên")
        break
    else:
        print("Không tìm thấy thông tin sinh viên")