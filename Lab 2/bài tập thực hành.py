# Bài 1
# Viết chương trình nhập vào một tháng, năm và cho biết tháng đó có bao nhiêu ngày?
#thang = int(input("Nhập vào tháng: "))
#if thang == 4 or thang == 6 or thang == 9 or thang == 11:
#    print("Tháng {} có 30 ngày".format(thang))
#elif thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
#    print("Tháng {} có 31 ngày".format(thang))
#elif thang == 2:
#    nam = int(input("Nhập vào năm: "))
#    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
#        print("Tháng 2 có 29 ngày")
#    else:
#        print("Tháng 2 có 28 ngày")
#else:
#    print("Mời nhập lại tháng")

# Bài 2
"""
Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc 2:
ax2 + bx + c = 0 (giải và biện luận đầy đủ các trường hợp)
"""
#a,b,c = map(int,input("Nhập vào hệ số của phương trình: ").split())
#if a == 0: 
#    if b == 0:
#        if c == 0:
#            print("Phương trình bậc nhất có vô số nghiệm")
#        else:
#            print("Phương trình bậc nhất vô nghiệm")
#    else:
#        x = -c/b
#        print("Phương trình bậc nhất có nghiệm là x =", x)
#else:
#    delta = b**2 - 4*a*c
#    if delta < 0:
#        print("Phương trình bậc hai vô nghiệm")
#    elif delta == 0:
#        x = -b/(2*a)
#        print("Phương trình bậc hai có nghiệm kép x1 = x2 =", x)
#    else:
#        x1 = (-b + delta**0.5)/(2*a)
#        x2 = (-b - delta**0.5)/(2*a)
#        print("Phương trình bậc hai có hai nghiệm phân biệt x1 = {} và x2 = {}".format(x1, x2))

# Bài 3
"""
Viết chương trình cho phép nhập vào thứ (từ 1 đến 7) trong tuần, 
nếu thứ không hợp lệ thì cho nhập lại. Sau đó cho biết thứ đã nhập có tên là gì và xuất kết quả ra màn hình (với 1: Chủ nhật, 2: Thứ hai, …)
"""
#thu = int(input("Nhập vào một thứ trong tuần: "))
#if thu == 1:
#    print("Chủ nhật")
#elif thu == 2:
#    print("Thứ hai")
#elif thu == 3: 
#    print("Thứ ba")
#elif thu == 4:
#    print("Thứ tư")
#elif thu == 5:
#    print("Thứ năm")
#elif thu == 6:
#    print("Thứ sáu")
#elif thu == 7:
#    print("Thứ bảy")
#else:
#    print("Xin mời nhập lại")

#Bài 4
# Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
#n = int(input("Nhập vào số nguyên: "))
#chu_so_hang_tram = n// 100 
#if chu_so_hang_tram == 0:
#    print("Số không có chữ số hàng trăm")
#elif 0 < chu_so_hang_tram <= 9:
#    print("Chữ số hàng trăm là:",chu_so_hang_tram)
#else:
#    phan_du = chu_so_hang_tram % 10
#    if phan_du == 0:
#        print("Chữ số hàng trăm là:",0)
#    else:
#        print("Chữ số hàng trăm là:",phan_du)

#Bài 6
#Viết chương trình nhập vào một số nguyên có ba chữ số. Hãy in ra cách đọc của số nguyên này.
n = int(input("Nhập vào số nguyên n: "))
if 100 <= n <= 999:
    chu_so_hang_tram = n // 100
    chu_so_hang_chuc = (n//10) % 10
    chu_so_hang_don_vi = n % 10
    # Đọc chữ số hàng trăm
    if chu_so_hang_tram == 1:
        doc_hang_tram = "một trăm"
    elif chu_so_hang_tram == 2:
        doc_hang_tram = 'hai trăm'
    elif chu_so_hang_tram == 3:
        doc_hang_tram = 'ba trăm'
    elif chu_so_hang_tram == 4:
        doc_hang_tram = 'bốn trăm'
    elif chu_so_hang_tram == 5:
        doc_hang_tram = 'năm trăm'
    elif chu_so_hang_tram == 6:
        doc_hang_tram = 'sáu trăm'
    elif chu_so_hang_tram == 7:
        doc_hang_tram = 'bảy trăm'
    elif chu_so_hang_tram == 8:
        doc_hang_tram = 'tám trăm'
    elif chu_so_hang_tram == 9:
        doc_hang_tram = 'chín trăm'
    elif chu_so_hang_tram == 0:
        doc_hang_tram = ''
    # Đọc chữ số hàng chục
    if chu_so_hang_chuc == 1:
        doc_hang_chuc = "mười"
    elif chu_so_hang_chuc == 2:
        doc_hang_chuc = 'hai mươi'
    elif chu_so_hang_chuc == 3:
        doc_hang_chuc = 'ba mươi'
    elif chu_so_hang_chuc == 4:
        doc_hang_chuc = 'bốn mươi'
    elif chu_so_hang_chuc == 5:
        doc_hang_chuc = 'năm mươi'
    elif chu_so_hang_chuc == 6:
        doc_hang_chuc = 'sáu mươi'
    elif chu_so_hang_chuc == 7:
        doc_hang_chuc = 'bảy mươi'
    elif chu_so_hang_chuc == 8:
        doc_hang_chuc = 'tám mươi'
    elif chu_so_hang_chuc == 9:
        doc_hang_chuc = 'chín mươi'
    elif chu_so_hang_chuc == 0:
        doc_hang_chuc = 'linh'
    # Đọc chữ số hàng đơn vị
    if chu_so_hang_don_vi == 1:
        doc_hang_don_vi = "một"
    elif chu_so_hang_don_vi == 2:
        doc_hang_don_vi = 'hai'
    elif chu_so_hang_don_vi == 3:
        doc_hang_don_vi = 'ba'
    elif chu_so_hang_don_vi == 4:
        doc_hang_don_vi = 'tư'
    elif chu_so_hang_don_vi == 5:
        doc_hang_don_vi = 'năm'
    elif chu_so_hang_don_vi == 6:
        doc_hang_don_vi = 'sáu'
    elif chu_so_hang_don_vi == 7:
        doc_hang_don_vi = 'bảy'
    elif chu_so_hang_don_vi == 8:
        doc_hang_don_vi = 'tám'
    elif chu_so_hang_don_vi == 9:
        doc_hang_don_vi = 'chín'
    elif chu_so_hang_don_vi == 0:
        doc_hang_don_vi = ''
    print("Số",n, "đọc là:", doc_hang_tram, doc_hang_chuc, doc_hang_don_vi)

# Bài 10
"""
Một điểm cho thuê sân tập bóng đá theo công thức sau:
+ Mỗi giờ trong 3 giờ đầu tiên tính 100.000 đồng/ giờ
+ Mỗi giờ tiếp theo có đơn giá giảm 25% so với đơn giá trong 3 giờ đầu tiên
+ Ngoài ra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá 10%
Viết chương trình nhập vào giờ bắt đầu, giờ kết thúc và in ra số tiền khách thuê sân 
tập phải trả, biết rằng 5 giờ <= giờ bắt đầu <= giờ kết thúc <= 22 giờ
"""
#gio_vao = int(input("Nhập giờ vào: "))
#gio_ra = int(input("Nhập giờ ra: "))
#thoi_gian_thue = gio_ra - gio_vao + 1
#tien_thue = 0
#if 5 <= gio_vao and gio_ra <= 22:
#    if 0 < thoi_gian_thue <= 3:
#        if 11 <= gio_vao < gio_ra <= 15:
#            tien_thue = 100000*thoi_gian_thue - 100000*thoi_gian_thue*0.1
#        else:
#            tien_thue = 100000 * thoi_gian_thue
#    elif thoi_gian_thue >= 3:
#        if 11 <= gio_vao < gio_ra <= 15:
#            tien_thue = (100000*thoi_gian_thue + (thoi_gian_thue - 3)*0.75)- (100000*thoi_gian_thue + (thoi_gian_thue - 3)*0.75 )*0.1
#        else:
#            tien_thue = 100000*thoi_gian_thue + (thoi_gian_thue - 3)*0.75 
#    print("Tiền thuê sân là:", tien_thue)
#else:
#    print("Giờ thuê sân không hợp lệ")

# Bài 11
"""
Cho trước số ngày trong một tháng của năm. 
Viết ra chương trình xuất ra ngày tiếp theo của 1 ngày cho trước.
"""
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if ngay == 31 and thang == 12:
    nam += 1
    print("Ngày tiếp theo là ngày 1 tháng 1 năm", nam)
elif (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    if ngay == 29 and thang == 2:
        print("Ngày tiếp theo là ngày 1 tháng 3 năm", nam)
    else:
        if ngay == 30 and (thang == 4 or thang == 6 or thang == 9 or thang == 11):
            thang += 1
            print("Ngày tiếp theo là ngày 1 tháng {} năm {}".format(thang, nam))
        elif ngay == 31 and (thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8):
            thang += 1
            print("Ngày tiếp theo là ngày 1 tháng {} năm {}".format(thang, nam))
        else:
            ngay += 1
            print("Ngày tiếp theo là ngày {} tháng {} năm {}".format(ngay, thang, nam))
elif ngay == 28 and thang == 2:
    print("Ngày tiếp theo là ngày 1 tháng 3", nam)
else:
    if ngay == 30 and (thang == 4 or thang == 6 or thang == 9 or thang == 11):
        thang += 1
        print("Ngày tiếp theo là ngày 1 tháng {} năm {}".format(thang, nam))
    elif ngay == 31 and (thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8):
        thang += 1
        print("Ngày tiếp theo là ngày 1 tháng {} năm {}".format(thang, nam))
    else:
        ngay += 1
        print("Ngày tiếp theo là ngày {} tháng {} năm {}".format(ngay, thang, nam)) 