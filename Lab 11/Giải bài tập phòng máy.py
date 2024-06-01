"""
Bài 1: 
Cho dãy các số nguyên dương được ghi trong tập tin dayso.dat. 
Hãy đọc các số hạng của dãy số này và tính tổng các số hạng lẻ trong dãy.
 Các số hạng có thể ghi trên nhiều dòng
"""
# Tạo tập tin gồm dãy các số nguyên
"""
n = int(input("Nhập số lượng số trong dãy số: "))
day_so = []
for i in range(1, n+1):
    so = int(input(f"Nhập số thứ {i}: "))
    day_so.append(str(so))

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/dayso.dat", "w", newline= "") as bai1:
    for so in day_so:
        bai1.write(so + "\n")

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/dayso.dat", "r") as bai1a:
    lines = bai1a.readlines()
# Chuyển các dòng thành số nguyên
data = []
for line in lines:
    num = int(line.strip())
    data.append(num)
sum = 0
for num in data:
    if num % 2 != 0:
        sum += num
print("Tổng các số lẻ có trong tập tin là:", sum)
"""

"""
Bài 8: 
Để quản lý nhân viên lưu trữ nội dung các thông tín dạng cấu trúc gồm: Mã NV, TênNV, Chức vụ, Hệ số lương, Lương, Phụ cấp chức vụ, Thực lĩnh.
Các thông tin Mã NV, Tên NV, Chức vụ, Hệ số lương 
được nhập vào từ bàn phím.
Tạo một project (thư mục) LAB11, có cấu trúc lưu trữ như sau:
Viết chương trình quản lý nhân viên đặt tên là qlynhanvien.py hiển thị menu để thựchiện các chức năng sau:
a) Nhập vào từ bàn phím một danh sách các nhân viên.
b) Tính Lương cho các nhân viên biết: Lương = Hệ số lương * 1 490 000.
Điền thông tin Phụ cấp chức vụ cho nhân viên biết:
+ Nếu Chức vụ là TP, phụ cấp chức vụ là 1 000 000.
+ Nếu Chức vụ là PP, phụ cấp là 700 000.
+ Nếu Chức vụ là NV, phụ cấp là 300 000. 
Điền thông tin Thực lĩnh cho nhân viên biết: Thực lĩnh = Lương + Phụ cấp chức vục.
c) In ra màn hình danh sách nhân viên với đây đủ thông tin dưới dạng bảng.
d) Sắp xếp danh sách nhân viên theo thứ tự giảm dần của Thực lĩnh và in ra danh sách sau sắp xếp.
e) Lưu dữ liệu vào file ds_nhanvien.csv trong thư mục files.
"""
import csv
def nhapthongtin():
    manv = input("Nhập thông tin mã nhân viên: ")
    tennv = input("Nhập tên nhân viên: ")
    chucvu = input("Nhập chức vụ của nhân viên: ")
    hesoluong = input("Nhập hệ số lương của nhân viên: ")
    return manv, tennv, chucvu, hesoluong

def luongnhanvien(hesoluong, chucvu):
    if chucvu == "Trưởng phòng":
        phucap = 1000000
    elif chucvu == "Phó phòng":
        phucap = 700000
    else:
        phucap = 300000
    luong = hesoluong * 1490000 + phucap
    return luong

def inthongtin(manv, tennv, chucvu, hesoluong, luong):
    print("Thông tin của nhân viên:")
    print("Mã nhân viên: ", manv)
    print("Tên nhân viên: ", tennv)
    print("Chức vụ nhân viên:", chucvu)
    print("Hệ số lương: ", hesoluong)
    print("Lương thực lĩnh: ", luong)

def main():
    n = int(input("Nhập số nhân viên: "))
    dulieu = []
    for i in range(1, n+1):
        nhanvien = {}
        print(f"Nhập thông tin của nhân viên thứ {i}")
        manv, tennv, chucvu, hesoluong = nhapthongtin()
        luong = luongnhanvien(hesoluong, chucvu)
        inthongtin(manv, tennv, chucvu, hesoluong, luong)
        nhanvien["Mã nhân viên"] = manv
        nhanvien["Tên nhân viên"] = tennv
        nhanvien["Chức vụ"] = chucvu
        nhanvien["Hệ số lương"] = hesoluong
        nhanvien["Lương thực lĩnh"] = luong
        dulieu.append(nhanvien)
    dulieu.sort(key = lambda x: x["Lương thực lĩnh"])
    print("Dữ liệu sau khi sắp xếp: ")
    print(dulieu)
    with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/ds_nhanvien.csv", "w") as bai8:
        fieldnames = ["Mã nhân viên", "Tên nhân viên", "Chức vụ", "Hệ số lương", "Lương thực lĩnh"]
        writer = csv.DictWriter(bai8, fieldnames = fieldnames)
        writer.writeheader()
        for nv in dulieu:
            writer.writerow(nv)

if __name__ == "__main__":
    main()



