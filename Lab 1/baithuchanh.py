# Bài 2
#s, m, h, d = map(int, input("Nhập các số đo").split())
#d_s = d * 24 * 60 * 60
#h_s = h * 60 * 60
#m_s = m * 60
#tong_thoi_gian = d_s + h_s + m_s + s 
#print("Tổng thời gian chuyển sang giây là", tong_thoi_gian)

#Diện tích xung quanh = chu vi đáy x chiều cao
#Diện tích toàn phần = diện tích xung quanh + diện tích 2 đáy
#Thể tích = diện tích đáy x chiều cao

# Bài 4
#x1, y1, z1 = map(int, input("Nhập tọa độ vecto a").split())
#x2, y2, z2 = map(int, input("Nhập tọa độ vecto b").split())
#ab = x1*x2 +y1*y2 + z1*z2
#print("Tích vô hướng của hai vecto a và b là:", ab)

#Bài 5
#s = float(input("Thời gian sử dụng bóng đèn: "))
#u = 220
#i = 2.7
#p = u *i
#cong_suat = (s*p)/1000
#print("Số tiền điện phải trả là:", cong_suat*7000)

#Bài 6
#a,b,c = map(int, input("Nhập các hệ số của phương trình bậc 2").split())
#delta = b**2 - 4*a*c
#x1 = (-b + delta**0.5)/(2*a)
#x2 = (-b - delta**0.5)/(2*a)
#print("Nghiệm của phương trình bậc 2 là: {:.2f} và {:.2f}".format(x1,x2))

#Bài 7
"""
x1, y1, z1 = map(int, input("Nhập vào tọa độ điểm A").split())
x2, y2, z2 = map(int, input("Nhập vào tọa độ điểm B").split())
x3, y3, z3 = map(int, input("Nhập vào tọa độ điểm C").split())
g_x = (x1 + x2 + x3)/3
g_y = (y1 + y2 + y3)/3
g_z = (z1 + z2 + z2)/3
m_x = (x1 + x2)/2
m_y = (y1 + y2)/2
m_z = (z1 + z2)/2
n_x = (x3 + x2)/2
n_y = (y3 + y2)/2
n_z = (z3 + z2)/2
p_x = (x3 + x1)/2
p_y = (y3 + y1)/2
p_z = (z3 + z1)/2
print("Tọa độ trọng tâm là ({},{},{})".format(g_x,g_y,g_z))
print("Tọa độ trung điểm AB là ({},{},{})".format(m_x,m_y,m_z))
print("Tọa độ trung điểm BC là ({},{},{})".format(n_x,n_y,n_z))
print("Tọa độ trung điểm AC là ({},{},{})".format(p_x,p_y,p_z))
"""

#Bài 9
#import math
#x = int(input("Nhập giá trị x:"))
#logarit cơ số 4 của x
#log1 = math.log(x, 4)
#logarit cơ số x của 2
#log2 = math.log(2, x)
#fx = log1 + log2
#print("Giá trị của biểu thức là", fx)