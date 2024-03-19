"""
Giả sử bạn đầu tư một số tiền ban đầu là 10.000 đô la vào một loại hình đầu tư
có lãi suất hàng năm là 6%. Hãy viết một chương trình Python để thực hiện các
tính toán sau và in kết quả ra màn hình (làm tròn đến số thập phân thứ hai)
"""
# Bài tổng quát với số tiền và lãi suất được nhập vào từ bàn phím
tien_goc = float(input("Nhập vào số tiền đầu tư ban đầu: "))
lai_suat = float(input("Nhập vào lãi suất tiền gửi: "))

# Tính toán số tiền sẽ có sau 5 năm và lưu kết quả vào biến amount_after_5_years
amount_after_5_years = tien_goc + (tien_goc * (1 + lai_suat/100)) ** 5

#Tính toán số tiền sẽ có sau 10 năm và lưu kết quả vào biến amount_after_10_years
amount_after_10_years = tien_goc + (tien_goc * (1 + lai_suat/100)) ** 10

# Tính toán tỷ lệ tăng trưởng của số tiền bạn sẽ có sau 10 năm so với số tiền bạn sẽ có sau 5 năm và lưu kết quả vào biến growth_rate
growth_rate = (amount_after_10_years - amount_after_5_years)/amount_after_5_years

# In kết quả ra màn hình, làm tròn tới chữ số thập phân thứ hai
print("Số tiền có được sau 5 năm là:", round(amount_after_5_years,2))
print("Số tiền có được sau 10 năm là:", round(amount_after_10_years,2))
print("Tỷ lệ tăng trưởng của số tiền sau 10 năm so với số tiền sau 5 năm là:", round(growth_rate,2))
