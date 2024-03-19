"""
Trong một gia đình, chiếc máy lọc không khí được kết nối với nguồn điện có
hiệu điện thế 220 V và hoạt động với cường độ dòng điện là 1,5 A. Hãy viết một
chương trình yêu cầu người dùng nhập vào số giờ sử dụng máy lọc không khí
(tính theo giờ). Chương trình sẽ tính và hiển thị tổng số tiền điện phải trả cho
việc sử dụng máy lọc không khí, với giá điện là 5000 đồng/kWh.
"""
thoi_gian_su_dung = float(input("Nhập thời gian sử dụng của máy lọc không khí (đơn vị giờ): "))

hieu_dien_the = 220 #đơn vị V
cuong_do_dong_dien = 1.5 # đơn vị A

# Tính công suất của máy lọc không khí
# Công suất = hiệu điện thế x cường độ dòng điện (đơn vị W)
cong_suat = hieu_dien_the * cuong_do_dong_dien

# Đổi đơn vị từ W sang kW
cong_suat_kw = cong_suat/1000

# Tính tiền điện phải trả
tien_dien = cong_suat_kw * thoi_gian_su_dung * 5000

# In kết quả ra màn hình
print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí với thời gian sử dụng {} giờ là {} đồng".format(thoi_gian_su_dung, tien_dien))