# Bài 1: Viết chương trình để in các số từ 1 đến 10
#a = 1 
#while a < 11:
#    print(a, end = " ")
#    a += 1

# Bài 2: Viết chương trình tìm ước chung lớn nhất (UCLN) của 2 số nguyên m và n. Áp dụng thuật toán Euclide.
"""
Ví dụ: m = 8 , n = 6
Vòng lặp 1:
m = 6
n = 2
Vòng lặp 2:
m = 2
n = 0
"""
#m, n = map(int, input("Nhập vào hai số nguyên m và n: ").split())
#if m > n:
#    while n != 0:
#        m, n = n, m % n
#    print("UCLN của 2 số là:", m)
#else:
#    while m != 0:
#        n, m = m, n % m
#    print("UCLN của 2 số là:", n)

# Bài 4: Viết chương trình nhập số n. Chương trình sẽ kết thúc nếu một trong các số đó là số âm
#while True:
#    n = int(input("Nhập vào một số: "))
#    if n < 0:
#        break
#    print(n)

"""
Bài 5: Viết chương trình nhập vào một số nguyên và in kết quả ra màn hình dưới dạng số đảo ngược 
(về thứ tự) của số nguyên vừa nhập đó.
Bước 1: Khởi tạo biến đảo ngược = 0
Bước 2: Tính phần dư = số ban đầu % 10
Bước 3: biến đảo ngược = biến đảo ngược * 10 + phần dư
Bước 4: cập nhật số ban đầu = số ban đầu // 10
Ví dụ: Tìm số đảo ngược của số 123 
so_dao_nguoc = 0 
so_ban_dau = 123
Tạo 1 vòng lặp:
Vòng lặp 1:
1. phần dư = 123 % 10 = 3 
2. cập nhật số đảo ngược = 0 * 10 + 3 = 3 
3. cập nhật số ban đầu = 123 // 10 = 12 
Vòng lặp 2:
1. phần dư: 12 % 10 = 2 
2. cập nhật số đảo ngược = 3 * 10 + 2 = 32
3. cập nhật số ban đầu = 12 // 10 = 1 
Vòng lặp 3:
1. phần dư: 1 % 10 = 1 
2. cập nhật số đảo ngược = 32 * 10 + 1 = 321
3. cập nhật số ban đầu = 1 // 10 = 0
"""
#n = int(input("Nhập vào số nguyên dương: "))
#so_dao_nguoc = 0
#while n != 0:
#    phan_du = n % 10
#    so_dao_nguoc = so_dao_nguoc * 10 + phan_du
#    n = n // 10
#print("Số đảo ngược của số đã cho là:", so_dao_nguoc)

# Bài 6: Viết chương trình kiểm tra một số n có là số nguyên tố
#n = int(input("Nhập vào số n: "))
#if n < 2:
#    print("Nhập lại số nguyên tố: ")
#else:
#    check = True
#    i = 2 
#    while i < n:
#        if n % i == 0:
#            check = False
#            break
#        i += 1
#    
#    if check == True:
#        print(n, "là số nguyên tố")
#    else:
#        print(n, "là không là số nguyên tố")

"""
Viết chương trình hiển thị một menu các chức năng của phép toán (cộng, trừ, nhân, chia) cho người dùng chọn, 
bấm số 0 để thoát.
"""
'''
a, b = map(int, input("Nhập vào hai số nguyên a và b: ").split())
print(
"""
Chương trình hiển thị menu phép tính:
    1. Phép cộng hai số
    2. Phép trừ hai số
    3. Phép nhân hai số
    4. Phép chia hai số
    0. Thoát chương trình
"""    
)
while True:
    lua_chon = int(input("Nhập vào lựa chọn: "))
    if lua_chon == 1:
        print(f"{a} + {b} = {a + b}")
        break
    elif lua_chon == 2:
        print(f"{a} - {b} = {a - b}")
        break
    elif lua_chon == 3:
        print(f"{a} x {b} = {a * b}")
        break
    elif lua_chon == 4:
        print(f"{a} : {b} = {a / b}")
        break
    elif lua_chon == 0:
        break
    else:
        print("Lựa chọn sai, vui lòng nhập lại")
'''

# Bài 8: Viết chương trình yêu cầu xuất ra các số từ 1 đến 100
#a = 1 
#while a <= 100:
#    print(a, end = " ")
#    if a % 20 == 0:
#        print() #Xuống dòng
#    a += 1    

"""
Bài 9:
Viết chương trình nhập ID và password
Chương trình sẽ lặp lại việc nhập ID và password cho đến khi user nhập đúng. 
Thao tác nhập được thực hiện ít nhất 1 lần.
"""
#id_goc = "HelloABC"
#password_goc = "ABC1234@"
#while True:
#    id = input("Nhập vào ID: ")
#    password = input("Nhập vào password: ")
#    if id == id_goc and password == password_goc:
#        print("Chương trình nhập đúng")
#        break
#    else: 
#        print("Nhập lại id và password")

# Bài 10: Viết chương trình in tất cả các số nguyên tố từ 1 đến n được nhập từ bàn phím.
#n = int(input("Nhập vào số n: "))
#a = 1
#print(f"Các số nguyên tố từ 1 đến {n} là:")
#while a <= n:
    # Kiểm tra a có phải số nguyên tố không
#    if a < 2:
#        pass
#        a += 1
#    else:
#        check = True
#        i = 2 
#        while i < a:
#            if a % i == 0:
#                check = False
#                break
#            i += 1
#        
#        if check == True:
#            print(a, end = " ")
#        a += 1