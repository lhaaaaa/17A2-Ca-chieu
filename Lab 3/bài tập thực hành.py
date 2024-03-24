# Bài 1
#n = int(input("Nhập vào số nguyên n: "))
#sum = 1 
#a = 1 
#for i in range(n+1):
#    a = a * ((2*(i+1))/(2*i+3))
#    sum = sum + a 
#print("Giá trị của biểu thức là:", sum)

# Bài 2: Viết chương trình tìm các số hoàn hảo nhỏ hơn n (Với n được nhập từ bàn phím)
#n = int(input("Nhập vào số nguyên n: "))
#if n < 0:
#    print("Xin mời nhập lại số n")
#else:
#    print(f"Các số hoàn hảo nhỏ hơn {n} là:")
#    for j in range(1,n): # Chạy vòng lặp j các số nhỏ n 
#        sum = 0
        # Tìm các ước nguyên dương của j
#        for i in range(1,j):
#            if j % i == 0:
#                sum = sum + i
        # Kiểm tra tổng sum với số n ban đầu
#        if sum == j:
#            print(j)

# Bài 3:
#1. Viết chương trình xét xem một số n có phải là số nguyên tố không. Nếu không phải hãy in ra số nguyên tố gần n nhất
#n = int(input("Nhập vào số nguyên n: "))
#if n < 2:
#    print("Xin mời nhập lại")
#else:
    #Kiểm tra n có phải là số nguyên tố
#    check = True # Giả sử n đang là số nguyên tố
    #Bắt đầu kiểm tra
#    for i in range(2,n):
#        if n % i == 0:
#            check = False # n không phải là số nguyên tố
    # Sau khi chạy hết vòng lặp, kiểm tra giá trị của biến check
#    if check == True:
#        print(f"{n} là số nguyên tố")
#    else:
#        for j in range(n-1,2,-1): #chuỗi số số giảm dần từ n - 1 đến 2
            # Kiểm tra j có phải số nguyên tố không
#            check = True # Giả sử j đang là số nguyên tố
            #Bắt đầu kiểm tra
#            for i in range(2,j):
#                if j % i == 0:
#                    check = False # j không phải là số nguyên tố
            # Sau khi chạy hết vòng lặp, kiểm tra giá trị của biến check
#            if check == True:
#                print(f"{j} là số nguyên tố nhỏ hơn và gần {n} nhất")
#                break

#2. Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n
#n = int(input("Nhập vào số nguyên n: "))
#for a in range(2,n+1):
    #Kiểm tra số a có phải là nguyên tố không?
#    check = True # Giả sử a đang là số nguyên tố
    #Bắt đầu kiểm tra
#    for i in range(2,a):
#        if a % i == 0:
#            check = False # a không phải là số nguyên tố
    # Sau khi chạy hết vòng lặp, kiểm tra giá trị của biến check
#    if check == True:
#        print(a)

# Bài 4
# Vẽ hình chữ nhật
#a = int(input("Nhập vào chiều rộng: "))
#b = int(input("Nhập vào chiều dài: "))
#for i in range(a):
#    for j in range(b):
#        print("* ", end='')
#    print()

# Bài 5
#n = int(input("Nhập vào số nguyên n: "))
#sum = 0
#for i in range(1,n+1):
#    sum = sum + i**3
#print(f"Tổng bậc 3 của {n} số nguyên đầu tiên là", sum)

# Bài 6
'''
n = int(input("Nhập vào số nguyên dương n: "))
sum = 0
if n <= 0:
    print("Xin mời nhập lại")
else:
    for i in range(1, n+1):
        S1 = sum + 1/i
    print("Tổng S1 là:",round(S1,2))

    for i in range(1, n+1):
        S2 = sum + i
    print("Tổng S2 là:", S2)

    for i in range(1, n+1):
        if i % 2 != 0:
            S3 = sum + i
    print("Tổng S3 là:", S3)

    for i in range(1, n+1):
        if i % 2 == 0:
            S4 = sum + i
    print("Tổng S4 là:", S4)

    for i in range(1, n+1):
        S5 = sum + i**2
    print("Tổng S5 là:", S5)

    for i in range(1, n+1):
        if i % 2 !=0:
            S6 = sum + i**3
    print("Tổng S6 là:", S6)

    for i in range(1, n+1):
        if i % 2 == 0:
            S7 = sum + i**4
    print("Tổng S7 là:", S7)
'''

# Bài 7: Viết chương trình nhập vào một số nguyên dương rồi xuất ra dạng phân tích thừa số nguyên tố của số đó.
#n = int(input("Nhập vào số nguyên dương n: "))

#for i in range(2, n+1):
#    if n % i == 0:
        # Kiểm tra số i có là số nguyên tố
#        check = True
#        for j in range(2,i):
#            if i % j == 0:
#                check = False
#        if check == True:
#            print(i)
#            n = n// i 