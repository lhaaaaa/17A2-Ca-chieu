# Bài 1
"""
Tính năm nhuận. Năm thứ n là nhuận nếu có 
Mệnh đề 1: chia hết cho 4, nhưng không chia hết cho 100 
hoặc (or)
Mệnh đề 2: chia hết cho 400 
"""
#n = int(input("Nhập vào năm cần kiểm tra: "))
#if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
#    print("Năm kiểm tra là năm nhuận")
#else:
#    print("Năm kiểm tra không phải là năm nhuận")

# Bài 2
"""
Viết chương trình kiểm tra xem điểm M(x, y) có nằm trong hình tròn 
tâm I(a, b) và bán kính R bằng cách xuất ra giá trị True nếu điểm M nằm 
trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn với x, y, a, b, R 
nhập vào từ bàn phím
Bước 1: Nhập vào tọa độ điểm M
Bước 2: Nhập vào tọa độ điểm I
Bước 3: Nhập vào bán kính R
Bước 4: Tính độ dài đoạn thẳng IM
Bước 5: Kiểm tra điều kiện
    + Nếu IM <= R: in ra "True"
    + Nếu IM > R: in ra "False"
"""

#Bài 3
"""
Viết chương trình nhập vào các số a, b, c sau đó kiểm tra bộ ba số a, b, c 
vừa nhập vào là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, 
tam giác vuông cân, tam giác đều hay không phải là bộ ba cạnh của tam giác.
"""
#a,b,c = map(int, input("Nhập vào số đo cần kiểm tra: ").split())
#if (a + b) > c and (a + c) > b and (b + c) > a: #Có phải tam giác không?
#    if (a == b) and (a == c) and (b == c): #Có phải tam giác đều không?
#        print("Bộ ba số đo lập thành tam giác đều")
#    elif (a == b) or (a == c) or (b == c): #Có phải tam giác cân không?
#        if (int(a**2 + b**2) == int(c**2)) or (int(a**2 + c**2) == int(b**2)) or (int(c**2 + b**2) == int(a**2)): #Có phải tam giác vuông cân không?
#            print("Bộ ba số đo lập thành tam giác vuông cân")
#        else:
#            print("Bộ ba số đo lập thành tam giác cân")
#    elif (int(a**2 + b**2) == int(c**2)) or (int(a**2 + c**2) == int(b**2)) or (int(c**2 + b**2) == int(a**2)): #Có phải tam giác vuông không?
#        print("Bộ ba số lập thành tam giác vuông")
#    else:
#        print("Bộ ba số lập thành tam giác thường")
#else:
#    print("Bộ ba số đo không lập thành tam giác")

# Bài 5
"""
Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm. 
Ký tự là bất kỳ được nhập từ bàn phím.
Kiểm tra ký tự nhập vào có phải là 1 trong các ký tự u,e,o,a,i,U,E,O,A,I
"""
#Bài 7
# Giải và biện luận nghiệm của hệ phương trình bậc nhất hai ẩn
#a1,b1,c1 = map(int, input("Nhập hệ số của phương trình 1: ").split())
#a2,b2,c2 = map(int, input("Nhập hệ số của phương trình 2: ").split())
#d = a1 * b2 - a2 * b1
#dx = b1 * c2 - b2 * c1
#dy = a1 * c2 - a2 * c1
#if d == 0:
#    if dx == dy == 0:
#        print("Hệ phương trình có vô số nghiệm")
#    else:
#        print("Hệ phương trình vô nghiệm")
#else:
#    x = dx/d
#    y = dy/d
#    print("Nghiệm của hệ phương trình là:", x, y)

#Bài 8
"""
Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
Nếu điểm A thì phân loại là sinh viên xuất sắc, điểm B là sinh viên loại giỏi, 
điểm C là sinh viên loại khá, điểm D là sinh viên loại trung bình, điểm E là sinh viên 
loại yếu, điểm F là sinh viên xếp loại kém.
"""

#Bài 9
"""
Tính cước taxi:
Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
+ Loại xe 4 chỗ:
Giá mở cửa: 11.000 đồng/0.8km   Trong phạm vi 20km: 12.100 đồng/km   Từ km thứ 21 trở đi: 10.000 đồng/km
+ Loại xe 7 chỗ:
Giá mở cửa: 13.000 đồng/0.8km	Trong phạm vi 30km: 14.000 đồng/km	 Từ km thứ 31 trở đi: 12.000 đồng/km
Tiền chờ: 5 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800 đồng/phút.
Loại xe chỉ nhập 4 hoặc 7.
"""
#loai_xe = int(input("Nhập vào loại xe: "))
#so_phut_cho = float(input("Nhập vào số phút chờ: "))
#so_km = float(input("Nhập số km đi được: "))
#tien_cho = 0
#if so_phut_cho > 5:
#    tien_cho = (so_phut_cho - 5)*800
#if loai_xe == 4:
#    if so_km < 0.8:
#        tien_xe = 11000
#    elif 0.8 <= so_km < 21:
#        tien_xe = 11000 + (so_km - 0.8)*12100
#    else:
#        tien_xe = 11000 + (20 - 0.8)*12100 + (so_km - 21)*10000
#    cuoc_taxi = tien_xe + tien_cho
#    print("Tiền cước taxi là: ", cuoc_taxi)
#elif loai_xe == 7:
#    if so_km < 0.8:
#        tien_xe = 13000
#    elif 0.8 <= so_km < 31:
#        tien_xe = 13000 + (so_km - 0.8)*14000
#    else:
#        tien_xe = 11000 + (30 - 0.8)*14000 + (so_km - 31)*12000
#    cuoc_taxi = tien_xe + tien_cho
#    print("Tiền cước taxi là: ", cuoc_taxi)
#else:
#    print("Loại xe không hợp lệ")

#Bài 10
"""
Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền lương thực sự mà nhân viên đó nhận được).
Với các thông tin giả sử như sau:
+ 30% thuế thu nhập nếu lương trên 15 triệu
+ 20% thuế thu nhập nếu lương từ 7 đến 15 triệu
+ 10% thuế thu nhập nếu lương dưới 7 triệu
"""
#luong_nhan_vien = float(input("Nhập tiền lương nhân viên (đơn vị triệu đồng): "))
#thue_thu_nhap = 0
#if luong_nhan_vien < 7:
#    thue_thu_nhap = luong_nhan_vien * 0.1
#elif 7<= luong_nhan_vien < 15:
#    thue_thu_nhap = luong_nhan_vien * 0.2
#else:
#    thue_thu_nhap = luong_nhan_vien * 0.3
#luong_rong = luong_nhan_vien - thue_thu_nhap
#print("Tiền lương nhân viên thực tế nhận là: {} triệu đồng".format(luong_rong))