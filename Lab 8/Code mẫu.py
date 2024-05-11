"""
# Hàm không có tham số
def xin_chao():
    print("Xin chào")

xin_chao()

# Hàm có tham số
def tong_2_so(so_thu_1, so_thu_2):
    tong = so_thu_1 + so_thu_2
    print("Tổng hai số là:", tong)

so_1 = 7
so_2 = 8
tong_2_so = tong_2_so(so_1, so_2)
"""
"""
# Biến cục bộ
def tong_2_so(so_thu_1, so_thu_2):
    tong = so_thu_1 + so_thu_2
    print("Tổng hai số là:", tong)

so_1 = 3
so_2 = 4
tong_2_so(so_1, so_2)
tong_moi = tong + 10
print(tong_moi)

# Biến toàn cục
def tong_2_so(so_thu_1, so_thu_2):
    global tong
    tong = so_thu_1 + so_thu_2
    print("Tổng hai số là:", tong)

so_1 = 3
so_2 = 4
tong_2_so(so_1, so_2)
tong_moi = tong + 10
print(tong_moi)
"""
"""
# Tham số bắt buộc
def in_thong_tin(ten, lop):
    print("Tên của sinh viên là", ten, "học lớp", lop)

in_thong_tin("Nam", "17A2")

# Tham số mặc định
def in_thong_tin(ten = "Nam", lop = "17A2"):
    print("Tên của sinh viên là", ten, "học lớp", lop)

in_thong_tin()

# Tham số theo tên
def in_thong_tin(ten, tuoi):
    print("Tên của sinh viên là", ten, "năm nay", int(tuoi), "tuổi")

in_thong_tin(tuoi = 23, ten = "Nam")

# Tham số có chiều dài thay đổi
def in_tuple(*args):
    for phan_tu in args:
        print(phan_tu)

in_tuple(1,2,3,4)

def in_dictionary(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

in_dictionary(name = "Nam", age = 23)
"""
"""
# Hàm lambda
square = lambda x: x**2
print(square(5))

# Hàm map
lst = [1,2,3,4,5,6,7,8,9,10]
lst_moi = list(map(lambda x: x**2, lst))
print(lst_moi)

# Hàm filter
lst_chan = list(filter(lambda x: x % 2 == 0, lst))
print(lst_chan)

# Hàm reduce
import functools
sum = functools.reduce(lambda x, y: x + y, lst)
print(sum)
"""