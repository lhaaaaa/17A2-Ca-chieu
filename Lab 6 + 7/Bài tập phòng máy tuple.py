"""
Bài 14:
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, 
name là string, age và score là number. Tuple được nhập vào bởi người dùng. 
Tiêu chí sắp xếp là: 
+ Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. 
+ Ưu tiên là tên > tuổi > điểm.
"""
sinh_vien = []
while True:
    a = int(input("Nhập số thứ tự của sinh viên: "))
    if a < 0:
        break
    name = input("Nhập tên của sinh viên: ")
    age = int(input("Nhập tuổi của sinh viên: "))
    score = float(input("Nhập điểm sinh viên: "))
    tp = (name,) + (age,) + (score,)
    sinh_vien.append(tp)
print(sinh_vien)
n = len(sinh_vien)
for i in range(n-1):
    for j in range(n - i - 1):
        if sinh_vien[j][0] > sinh_vien[j+1][0]: #Kiểm tra theo tên
            sinh_vien[j], sinh_vien[j+1] = sinh_vien[j+1],sinh_vien[j]
        elif sinh_vien[j][0] == sinh_vien[j+1][0]:
            if sinh_vien[j][1] > sinh_vien[j+1][1]: #Kiểm tra theo tuổi
                sinh_vien[j], sinh_vien[j+1] = sinh_vien[j+1],sinh_vien[j]
            elif sinh_vien[j][1] == sinh_vien[j+1][1]:
                if sinh_vien[j][2] > sinh_vien[j+1][2]: # Kiểm tra theo điểm
                    sinh_vien[j], sinh_vien[j+1] = sinh_vien[j+1],sinh_vien[j]
print(sinh_vien)