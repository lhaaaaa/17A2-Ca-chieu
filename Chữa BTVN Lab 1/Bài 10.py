"""
Trong một hộp có 50 viên bi, bao gồm 20 viên bi đỏ, 15 viên bi xanh và 15 viên
bi vàng. Viết chương trình yêu cầu người dùng nhập vào số lượng viên bi mà
họ muốn rút ra từ hộp mà không nhìn và tính xác suất để trong số các viên bi
được rút ra:
1. Tất cả là bi đỏ.
2. Ít nhất một viên là bi xanh.
3. Đúng hai viên là bi vàng.
Chương trình hiển thị kết quả xác suất cho mỗi trường hợp, làm tròn đến bốn
chữ số sau dấu phẩy. 
"""
# Công thức tổ hợp chập k của n trong Python được sử dụng bởi thư viện math: math.comb(n,k)
import math
# Nhập vào số viên bi muốn rút
so_vien_bi = int(input("Nhập số lượng viên bi muốn rút: "))

# Không gian mẫu
khong_gian_mau = math.comb(50, so_vien_bi)

# Tất cả viên bi lấy ra là màu đỏ
y_1 = math.comb(20, so_vien_bi)
xac_suat_y_1 = y_1/khong_gian_mau

# Ít nhất một viên là bi xanh. Lấy xác suất đối: không có viên bi xanh
# TH1: toàn bộ số bi lấy ra là màu đỏ
bi_do = math.comb(20, so_vien_bi)
# TH2: toàn bộ số bi lấy ra là màu vàng
bi_vang = math.comb(15, so_vien_bi)
# TH3: số viên bi lấy ra có màu đỏ và màu vàng
bi_do_va_vang = math.comb(35, so_vien_bi)
doi_y_2 = bi_do + bi_vang + bi_do_va_vang
xac_suat_y_2 = 1 - doi_y_2/khong_gian_mau 

# Đúng 2 viên bi vàng
so_vien_bi_do_xanh = so_vien_bi - 2 
y_3 = math.comb(15, 2) * math.comb(35, so_vien_bi_do_xanh)
xac_suat_y_3 = y_3/khong_gian_mau

# In kết quả ra màn hình
print(
"""
Xác suất lấy {} viên bi từ hộp trong đó tất cả bi là đỏ là: {:.4f}
Xác suất lấy {} viên bi từ hộp trong đó ít nhất một viên bi xanh là: {:.4f}
Xác suất lấy {} viên bi từ hộp trong đó có đúng 2 viên bi vàng là: {:.4f}
""".format(so_vien_bi, xac_suat_y_1, so_vien_bi, xac_suat_y_2, so_vien_bi,xac_suat_y_3)
)
