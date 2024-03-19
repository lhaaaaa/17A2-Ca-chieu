"""
Viết chương trình nhập vào tọa độ của 2 vecto a và b. Tính và in ra mà hình:
1. Phép cộng vecto a + b, phép trừ vecto a – b
2. Độ dài của vecto a, độ dài của vecto b 
3. Cosin góc hợp giữa hai vecto a và b (làm tròn đến 2 chữ số thập phân)
"""
import math 
# Nhập vào tọa độ của vecto a
x1, y1 = map(float, input("Nhập vào tọa độ của vecto a: ").split())
# Nhập vào tọa độ của vecto b
x2, y2 = map(float, input("Nhập vào tọa độ của vecto b: ").split())
# Phép cộng vecto
x_phep_cong = x1 + x2
y_phep_cong = y1 + y2
# Phép trừ vecto
x_phep_tru = x1 - x2
y_phep_tru = y1 - y2
# Độ dài vecto a 
do_dai_vecto_a = (x1**2 + y1**2)**0.5
# Độ dài vecto b
do_dai_vecto_b = math.sqrt(x2**2 + y2**2)
# Cosin góc hợp giữa hai vecto a và b
# Cosin = tích vô hướng/ tích độ dài
tich_vo_huong = x1 * x2 + y1 * y2
tich_do_dai = do_dai_vecto_a * do_dai_vecto_b
cosin = tich_vo_huong/tich_do_dai
# In kết quả ra màn hình
print("Phép cộng vecto a = ({},{}) với vecto b = ({},{}) là: ({},{})".format(x1,y1,x2,y2,x_phep_cong,y_phep_cong))
print("Phép trừ vecto a = ({},{}) cho vecto b = ({},{}) là: ({},{})".format(x1,y1,x2,y2,x_phep_tru,y_phep_tru))
print("Độ dài vecto a = ({},{}) là: {:.2f}".format(x1,x2,do_dai_vecto_a))
print("Độ dài vecto b = ({},{}) là: {:.2f}".format(x1,x2,do_dai_vecto_b))
print("Cosin góc hợp giữa 2 vecto a và b là", round(cosin,2))
