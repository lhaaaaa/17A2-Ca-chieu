"""
Bài 1: 
a) Viết chương trình khởi tạo một set với các phần tử là ký tự 
được nhập từ bàn phím. Việc nhập dữ liệu kết thúc khi nhập vào ký tự “q”. 
Xóa các phần tử là ký tự số khỏi tập hợp.
b) Viết chương trình tạo danh sách Numbers các phần tử là số tự nhiên 
nhập từ bàn phím và sinh một tập hợp A với các phần tử thuộc danh sách Numbers.
c) Viết chương trình sinh một tập hợp A một cách ngẫu nhiên gồm n
số thực (n được nhập từ bàn phím). Tìm phần tử nhỏ nhất, lớn nhất và 
tổng các phần tử của tập hợp A.

A = set()
while True:
    kytu = input("Nhập ký tự từ bàn phím: ")
    if kytu == "q":
        break
    A.add(kytu)
print(A)
B = set()
for kytu in A:
    if kytu not in "0123456789":
        B.add(kytu)
print(B)

numbers = []
while True:
    so = int(input("Nhập số từ bàn phím: "))  
    if so < 0:
        break
    numbers.append(so)
print(numbers)
A = set(numbers)
print(A)

A = set()
import random
n = int(input("Nhập một số từ bàn phím: "))
for i in range(n):
    so = random.randint(1,1000)
    A.add(so)
print(A)
print("Phần tử nhỏ nhất trong tập hợp A là:", min(A))
print("Phần tử lớn nhất trong tập hợp A là:", max(A))
sum = 0
for so in A:
    sum += so
print("Tổng các phần tử trong tập hợp A là:", sum)
"""

"""
a) Viết chương trình sinh ngẫu nhiên 2 tập hợp A, B là các ký tự chữ 
và số được nhập từ bàn phím sau đó liệt kê ra màn hình các phần tử chung 
của A, B.
b) Viết chương trình sinh tập hợp A bao gồm cả số nguyên, số thực và chuỗi ký 
tự. Hãy đếm số phần tử là số nguyên, số thực và chuỗi ký tự của tập hợp A.
c) Viết chương trình thực hiện các công việc sau:
+ Nhập một số tự nhiên n từ bàn phím
+ Tạo 2 tập hợp A, B, trong đó A là tập các số nguyên tố là ước của n; 
Tập hợp B bao gồm các số nguyên tố nhỏ hơn n và không là ước của n.

A = set()
B = set()
while True:
    kytuA = input("Nhập vào một ký tự: ")
    if kytuA == 'q':
        break
    soA = float(input("Nhập một số: "))
    A.add(kytuA)
    A.add(soA)
print(A)
B = set()
while True:
    kytuB = input("Nhập vào một ký tự: ")
    if kytuB == 'q':
        break
    soB = float(input("Nhập một số: "))
    B.add(kytuB)
    B.add(soB)
print(B)

# Sử dụng itersection
C = A.intersection(B)
print(C)

D = set()
# Không sử dụng intersection
for i in A:
    for j in B:
        if i == j:
            D.add(i)
print(D)


A = set()
while True:
    a = input("Nhập vào một ký tự: ")
    if a == "q":
        break
    b = int(input("Nhập vào một số nguyên: "))
    c = float(input("Nhập vào một số thực: "))
    A.add(a)
    A.add(b)
    A.add(c)
print(A)
count1 = 0
count2 = 0
count3 = 0
for kytu in A:
    if type(kytu) == int:
        count1 += 1 
    elif type(kytu) == float:
        count2 += 1 
    elif type(kytu) == str:
        count3 += 1
print("Số lượng phần tử là số nguyên trong tập A là:", count1)
print("Số lượng phần tử là số thực trong tập A là:", count2)
print("Số lượng phần tử là xâu ký tự trong tập A là:", count3)
"""
n = int(input("Nhập một số từ bàn phím: "))
list_uoc = []
A = set()
for i in range(1,n):
    if n % i == 0:
        list_uoc.append(i)
for so in list_uoc:
    check = True
    if so < 2:
        continue
    else:
        for i in range(2, so):
            if so % i == 0:
                check = False
        if check == True:
            A.add(so)
print(A)
B = set()
for i in range(n):
    if i < 2:
        continue
    else:
        check = True
        for j in range(2,i):
            if i % j == 0:
                check = False
        if check == True: 
            if i in A:
                continue
            else:
                B.add(i)
print(B)




