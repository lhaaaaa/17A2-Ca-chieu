"""
Viết chương trình để tính toán diện tích xung quanh, diện tích toàn phần và thể
tích của một hình chóp tứ giác đều. Người dùng sẽ nhập vào độ dài cạnh đáy
và chiều cao của hình chóp từ bàn phím (làm tròn đến số thập phân thứ hai)
"""
# Nhập độ dài cạnh đáy và chiều cao của hình chóp tứ giác đều
canh_day = float(input("Nhập độ dài cạnh đáy của hình chóp: "))
chieu_cao = float(input("Nhập độ cao của hình chóp: "))

# Tính toán diện tích xung quanh của hình chóp tứ giác đều
# Diện tích xung quanh = 1/2 x chu vi đáy x chiều cao = 1/2 x 4 x cạnh đáy x chiều cao
Sxq = 1/2 * 4 * canh_day * chieu_cao

# Tính toán diện tích toàn phần của hình chóp tứ giác đều
# Diện tích toàn phần = diện tích xung quah +  diện tích đáy
Stp = Sxq + canh_day ** 2

# Tính toán thể tíc của hình chóp tứ giác đều
# Thể tích = 1/3 x diện tích đáy x chiều cao
the_tich = 1/3 * (canh_day ** 2) * chieu_cao

# In các tính toán
# Sử dụng round
print("Diện tích xung quanh của hình chóp tứ giác đều là:", round(Sxq,2))
# Sử dụng format
print("Diện tích toàn phần của hình chóp tứ giác đều là: {:.2f}".format(Stp))
# Sử dụng f-string
print(f"Thể tích của hình chóp tứ giác đều là: {the_tich:.2f}")
