# Bài 1: Viết chương trình tính tổng của dãy các số từ 1 đến 200.
#sum = 0
#for i in range(1,201):
#    sum = sum + i
#print("Giá trị tổng là:",sum)

# Bài 2: Viết chương trình in ra màn hình dãy số lẻ bé hơn một số n nào đó được nhập vào từ bàn phím
#n = int(input("Nhập vào số nguyên n: "))
#print(f"Các số lẻ bé hơn {n} là:")
#for i in range(n):
    # Kiểm tra số i có phải là số lẻ không
#    if i % 2 != 0:
#        print(i)

# Bài 7
#n = int(input("Nhập vào chiều cao của tam giác: "))
# Vẽ tam giác vuông câu a
#for i in range(1, n+1):
#    print("* "*i)

#Vẽ tam giác vuông câu b
#for i in range(1, n+1):
#    # In ra các khoảng trắng
#    for j in range(n-i+1):
#        print(" ", end="")
    # In ra ký tự *
#    for j in range(i):
#        print("*", end="")
    # Xuống dòng
#    print()

#Vẽ tam giác cân câu c
#for i in range(1, n+1):
    # In ra các khoảng trắng:
#    for j in range(n-i):
#        print(' ',end ='')
    # In ra ký tự *
#    for j in range(i):
#        print("* ", end ='')
    # Xuống dòng 
#    print()

# Vẽ tam giác câu d
#for i in range(1, n+1):
#    for j in range(1,i+1):
#        print(j, end = ' ')
#    # Xuống dòng
#    print()

# Vẽ tam giác câu e
#a = 1
#for i in range(1, n+1):
#    for j in range(1, i+1):
#        print(a, end = " ")
#        a += 1
    # Xuống dòng 
#    print()

# Vẽ tam giác câu e
#ky_tu_ban_dau = "A"
#for i in range(1, n+1):
#    for j  in range(1, i+1):
#        print(ky_tu_ban_dau, end=' ')
    # Xuống dòng
#    print()
#    ky_tu_ban_dau = chr(ord(ky_tu_ban_dau)+1)

# Bài 6: In bảng cửu chương
#n = int(input("Nhập vào số nguyên dương n: "))
#for i in range(1, 16):
#    tich = n * i
#    print(f"{n} x {i} = {tich}")

# Bài 8: Viết chương trình tìm ước chung lớn nhất của 2 số nguyên được nhập vào từ bàn phím
#a = int(input("Nhập vào số nguyên a: "))
#b = int(input("Nhập vào số nguyên b: "))
# Tìm số nhỏ hơn trong 2 số a và b
#min = a 
#UCLN = 1
#if min > b:
#    min = b 
#for i in range(1, min):
#    if a % i == 0 and b % i == 0:
#        UCLN = i
#print(f"UCLN của 2 số {a} và {b} là: {UCLN}")

"""
Bài 9: Viết chương trình liệt kê tất cả các số nguyên tố có 2 chữ số và 
tính tổng tất cả các số nguyên tố đó. Cho biết có bao nhiêu số nguyên tố có 2 chữ số?
"""
'''
count = 0
sum = 0
for i in range(10, 100):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
    if check == True:
        print(i, end =' ')
        sum = sum + i
        count += 1
print()
print("Tổng các số nguyên số có 2 chữ số là:", sum)
print("Số lượng các số nguyên tố có 2 chữ số là:",count)
'''