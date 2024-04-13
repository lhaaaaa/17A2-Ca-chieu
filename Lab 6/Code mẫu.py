# Khởi tạo list
#danh_sach = [8, 9.0, "abc", True]
#print(danh_sach)

# Độ dài của list
#print(len(danh_sach))

# Truy cập vào từng chỉ mục bên trong list
#for i in range(len(danh_sach)):
#    print(danh_sach[i])

# Tryt cập vào từng phần tử bên trong list
#for i in danh_sach:
#   print(i)
 
# Thêm phần tử vào list
# Sử dụng append 
#danh_sach.append(6) # Thêm phần tử vào cuối list
#print(danh_sach)
#danh_sach.insert(1, 6)
#print(danh_sach)

# Xóa phần tử khỏi list
# Sử dụng remove
#danh_sach.remove("abc")
#print(danh_sach)

# Sử dụng pop
#print(danh_sach.pop(2))

# Sử dụng del
#del danh_sach
#print(danh_sach)

# Sử dụng clear
#danh_sach.clear()
#print(danh_sach)

# Truy cập các phần tử trong list
#print(danh_sach[0])
#print(danh_sach[:3])
#print(danh_sach[-1])

# Cập nhật các phần tử trong list
#danh_sach[3] = False
#print(danh_sach)

# Không sử dụng hàm max()
#danh_sach = [6, 2, 4, 5, 9]
#max = 0 
#for i in danh_sach:
#    if max < i:
#        max = i
#print(max)
#print(max(danh_sach))

# Sắp xếp list
#danh_sach.sort()
#danh_sach.sort(reverse = True)
#print(danh_sach)
#a = sorted(danh_sach)
#print(danh_sach)
#print(a)

# List comprehension
#n = int(input("Nhập số phần tử: "))

#danh_sach = []
#for i in range(n):
#    a = input("Nhập vào giá trị: ")
#    danh_sach.append(a)
#print(danh_sach)

#danh_sach1 = [input(f"Nhập vào giá trị thứ {i+1}: ") for i in range(n)]
#print(danh_sach1)

#danh_sach2 = [x**2 for x in range(5)]
#print(danh_sach2)

#danh_sach3 = [x**2 for x in range(5) if x % 2 == 0]
#print(danh_sach3)

# Khai báo một ma trận
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]"))
        row.append(a)
    matrix.append(row)
print(matrix)

print(matrix[2][0])

