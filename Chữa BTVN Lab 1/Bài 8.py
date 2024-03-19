import math
# Tính giá trị của biểu thức
x, z = map(float, input("Nhập vào các số x, z thỏa mãn: ").split())

# Viết biểu thức và tính giá trị
tu = (x**2) * math.sin(z) + math.sqrt(abs(z))
mau = math.log(z) + math.e**(x-1)
fxz = tu/mau + math.atan(x*z)

# In kết quả ra màn hình
print("Giá trị của biểu thức là:", round(fxz,2))