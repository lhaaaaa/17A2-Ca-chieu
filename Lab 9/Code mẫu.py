# Hàm đệ quy
def factorial(n):
    if n == 0:
        return 1  # Điều kiện cơ sở: giai thừa của 0 là 1
    else:
        return n * factorial(n - 1)  # Điều kiện dừng: nếu n > 0, tiếp tục đệ quy

result = factorial(5)
print(result)

# Tính giai thừa bằng 3 cách
import time
# Không sử dụng hàm
n = 30
start1 = time.time()
tich1 = 1
for i in range(1, n+1):
    tich1 *= i
print(tich1)
end1 = time.time()
print("Thời gian chạy Cách 1:", end1 - start1)

# Sử dụng hàm thông thường
def giai_thua1(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich
start2 = time.time()
print(giai_thua1(n))
end2 = time.time()
print("Thời gian chạy Cách 2:", end2 - start2)

# Sử dụng hàm đệ quy
def giai_thua2(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua2(n-1)
start3 = time.time()
print(giai_thua2(n))
end3 = time.time()
print("Thời gian chạy Cách 3:", end3 - start3)
