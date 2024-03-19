"""
Viết chương trình để quản lý thông tin sách trong một thư viện. Chương trình
cho phép người dùng nhập vào các thông tin của một cuốn sách bao gồm: mã
sách, tên sách, tác giả, năm xuất bản, số lượng sách
Yêu cầu: In ra màn hình dòng lệnh:
Thư viện ĐHKTKTCN có {số lượng sách} sách {tên sách} với mã số {mã sách}.Cuốn sách của tác giác {tác giả} được xuất bản vào năm {năm xuất bản}
"""

# Chương trình nhập vào các thông tin của cuốn sách
print("---Nhập thông tin của cuốn sách---")
ma_sach = input("Nhập mã sách: ")
ten_sach = input("Nhập tên sách: ")
tac_gia = input("Nhập tên tác giả: ")
nam_xuat_ban = input("Nhập năm xuất bản cuốn sách: ")
so_luong = int(input("Nhập số lượng sách: "))
print("---Dòng lệnh theo yêu cầu:----")
print(f"Thư viện ĐHKTKTCN có {so_luong} sách {ten_sach} với mã số {ma_sach}. Cuốn sách của tác giác {tac_gia} được xuất bản vào năm {nam_xuat_ban}")