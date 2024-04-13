"""
Bài 1: 
Cho danh sách a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8] gồm n = 10 phần tử.
Yêu cầu:
+ Tính tổng các phần tử của danh sách.
+ Đếm số lượng các số hạng dương và tổng của các số hạng dương.
+ Tìm vị trí của phần tử âm đầu tiên trong danh sách.
+ Tìm vị trí của phần tử dương cuối cùng trong danh sách.
+ Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất đó.

danh_sach = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
sum = 0 
for i in danh_sach:
    sum += i
print("Tổng các phần tử của danh sách là:", sum)

count = 0
sum_pos = 0
for i in danh_sach:
    if i > 0:
        sum_pos += i
        count += 1
print(f"Số các số hạng dương trong dãy là {count} và có tổng bằng {sum_pos}")

for i in range(len(danh_sach)):
    if danh_sach[i] < 0:
        print("Vị trí phần tử âm đầu tiên trong danh sách là:", i+1)
        break

for i in range(len(danh_sach)-1, -1, -1):
    if danh_sach[i] > 0:
        print("Vị trí phần tử dương cuối cùng trong danh sách là:", i+1)
        break

max = 0 
vi_tri = 0
for i in range(len(danh_sach)):
    if max < danh_sach[i]:
        max = danh_sach[i]
        vi_tri = i + 1
print(f"Giá trị lớn nhất của dãy là {max} ở vị trí {vi_tri}")
"""

"""
Bài 2: 
Viết chương trình nhập vào một danh sách các phần tử là nguyên 
với số phần tử bằng n (n nhập từ bàn phím). Thực hiện các yêu cầu sau.
+ Tìm phần tử lớn thứ hai của danh sách và vị trí của phần tử đạt giá trị lớn thứ hai.
+ Tính số lượng các số dương liên tiếp nhiều nhất.
+ Tính số lượng các số dương liên tiếp có tổng lớn nhất.
"""
"""
n = int(input("Nhập số nguyên từ bàn phím: "))
danh_sach = [int(input(f"Nhập giá trị phần tử thứ {i+1}: ")) for i in range(n)]
print(danh_sach)
# Cách 1: 
danh_sach_copy = danh_sach.copy()
max = max(danh_sach_copy)
danh_sach_copy.remove(max)
max2 = 0
vi_tri = 0
for i in range(len(danh_sach_copy)):
    if max2 < danh_sach_copy[i]:
        max2 = danh_sach_copy[i]
        vi_tri = i + 1
print(f"Phần tử lớn thứ hai của danh sách là {max2} ở vị trí thứ {vi_tri}")

# Cách 2:
a = sorted(danh_sach)
vi_tri2 = 0
for i in range(len(danh_sach)):
    if danh_sach[i] == a[-2]:
        vi_tri2 = i + 1
print(f"Phần tử lớn thứ hai của danh sách là {a[-2]} ở vị trí thứ {vi_tri2}")

count = 0
for i in range(n):
    if danh_sach[i] > 0:
        count += 1
    elif danh_sach[i] < 0:
        if danh_sach[i] == danh_sach[-1]:
            break
        count = 0
print("Số lượng các số dương liên tiếp nhiều nhất là:", count)
"""

"""
Bài 3: 
Viết chương trình nhập vào một danh sách các phần tử là số nguyên cho đến khi nhập vào số 0. 
Thực hiện các yêu cầu sau.
+ Chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình.
+ Chèn một số m (m nhập vào từ bàn phím) vào đầu danh sách, cuối danh sách và vị trí thứ 5 của danh sách.

danh_sach = [] 
while True:
    a = int(input("Nhập vào phần tử của dãy: "))
    if a != 0:
        danh_sach.append(a)
    else:
        break
print(danh_sach)

i = 0
j = len(danh_sach) - 1
while i < j:
    if danh_sach[i] > 0:
        i += 1
    elif danh_sach[j] <= 0:
        j -= 1
    else:
        danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
        i += 1
        j -= 1
print("Danh sách sau khi sắp xếp là:", danh_sach)

m = int(input("Nhập số cần chèn: "))
# Vị trí cuối dãy
danh_sach.append(m)
# Vị trí đầu dãy
danh_sach.insert(0, m)
# Vị trí thứ 5 của dãy
danh_sach.insert(4, m)
print(danh_sach)
"""

"""
Bài 9: 
Viết chương trình sử dụng module random và list comprehension 
để xuất một số ngẫu nhiên, chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200).

import random
danh_sach = [random.randrange(0,201) for _ in range(20)]
print(danh_sach)
for i in danh_sach:
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        break
"""

"""
Bài 16:
1. Viết chương trình sinh dãy (list) A là biểu diễn của ma trận đơn vị. Chương trình nhập số n từ bàn phím và sinh ra ma trận đơn vị bậc n, sau đó hiện kết quả trên màn hình.
2. Ma trận mxn (m hàng, n cột) có thể được mô tả bởi danh sách như sau:
A=|[all, al2, ...aln], [a21, a22,...,a2n], ...,[am1, am2, ..., amn]].
Thực hiện các công việc sau:
a) Viết chương trình nhập vào ma trận A với các phần tử aij là các số tự nhiên được nhập từ bàn phím.
b) Tính tổng các phần tử của Ma trận A.
"""
"""
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        if i == j:
            a = 1 
            row.append(a)
        else:
            a = 0
            row.append(a)
    matrix.append(row)
print(f"Ma trận đơn vị cỡ {m} x {n} là: {matrix}")

matrix2 = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]: "))
        row.append(a)
    matrix2.append(row)
print(matrix2)

sum = 0
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        sum += matrix2[i][j]
print("Tổng của các phần tử của ma trận là:", sum)
"""

"""
Bài 12:
Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong 
["'Anh", "Em"], động từ nằm trong ("'Chơi", "Yêu"] và tân ngữ là ["Bóng đá", "Bóng rổ"].

chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]
cau = ""
for a in chu_ngu:
    for b in dong_tu:
        for c in tan_ngu:
            cau = a + " " + b + " " + c 
            print(cau)
"""

"""
Bài 10:
Viêt chương trình tạo một danh sách A có n phần tử là số nguyên được nhập từ bàn phím. Sử dụng List Comprehension thực hiện các yêu cầu sau:
a) Tạo ra một danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách ban đầu. In kết quả ra màn hình.
b) Tạo một danh sách C với các phần tử là bình phương của danh sách A.
c) Tạo ra danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3.

import random
n = int(input("Số phần tử: "))
danh_sach_A = [int(input("Nhập vào phần tử trong danh sách: ")) for _ in range(n)]
print(danh_sach_A)

danh_sach_B = [a for a in danh_sach_A if (a % 3 == 0) and (a % 5 != 0)]
print(danh_sach_B)

danh_sach_C = [a**2 for a in danh_sach_A]
print(danh_sach_C)

danh_sach_D = [random.choice(danh_sach_A) for a in range(len(danh_sach_A)) if a % 3 == 0]
print(danh_sach_D)
"""

"""
Bài 5: 
1. Viết chương trình sinh một dãy list A gồm 10 số tự nhiên, nằm ngẫu nhiên trong khoảng [1,99999]
2. Viết chương trình sinh một dãy list A gồm 10 số tự nhiên, nằm ngẫu nhiên trong khoảng [1,99999]. Sau đó sắp xếp lại theo thứ tự tăng dần theo 2 cách. Sử dụng hàm sorted() và không sử dụng hàm sorted().

import random
danh_sach_A = [random.randrange(1,100000) for _ in range(10)]
print(danh_sach_A)
# Sử dụng hàm sorted 
danh_sach_A_sx = sorted(danh_sach_A)
print(danh_sach_A_sx)
# Không sử hàm sorted
for i in range(len(danh_sach_A)):
    for j in range(i, len(danh_sach_A)):
        if danh_sach_A[i] > danh_sach_A[j]:
            danh_sach_A[i], danh_sach_A[j] = danh_sach_A[j], danh_sach_A[i]
print(danh_sach_A) 
"""

"""
Bài 6: 
Giả sử có một danh sách như sau:
List _= [["'mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
Yêu cầu:
+ Tạo danh sách List_ và in các phần tử của List_ ra màn hình
+ Chọn ra phần tử thứ hai, thuộc vị trí thứ 3 của sublist.
+ Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên.
+ Thực hiện tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật.

List_= [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for i in range(len(List_)):
    for j in range(len(List_[i])):
        print(List_[i][j], end = " ")
print()
print(List_[3][1])

sale_value = 0 
for i in range(len(List_)):
    if List_[i][0] == "mon" or List_[i][0] == "tue" or List_[i][0] == "sat" or List_[i][0] == "sun":
        sale_value += List_[i][1]
print("Tổng sale value là:", sale_value)
"""

"""
Bài 7: 
Với n được nhập vào từ bàn phím. Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ","
Ví dụ: Nếu n được nhập là 7 thì chương trình sẽ in ra: 0, 1, 1, 2, 3, 5, 8, 13.

n = int(input("Nhập vào số n: "))
fib_lst = [0, 1]
[fib_lst.append(fib_lst[-1] + fib_lst[-2]) for _ in range(2,n + 1)]
print(fib_lst)
"""