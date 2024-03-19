"""
Viết chương trình yêu cầu người dùng nhập vào các hệ số a1, b1, c1, a2, b2, và
c2 của một hệ phương trình bậc nhất hai ẩn gồm hai phương trình sau đây:
a1x + b1y = c1
a2x + b2y = c2
Sau đó, chương trình hiển thị kết quả của hệ phương trình trên. Kết quả nên
được làm tròn đến hai chữ số sau dấu phẩy.
"""
# Nhập vào hệ số của phương trình thứ nhất
a1, b1, c1 = map(float, input("Nhập các hệ số của phương trình thứ nhất: ").split())

# Nhập vào hệ số của phương trình thứ hai
a2, b2, c2 = map(float, input("Nhập các hệ số của phương trình thứ hai: ").split())

# Tính cách định thức
d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1 
dy = a1 * c2 - a2 * c1

# Tính nghiệm của hệ phương trình bậc nhất hai ẩn
x = d/dx
y = d/dy

# In kết quả ra màn hình
print("Nghiệm của hệ phương trình bậc nhất hai ẩn là: (x,y) = ({:.2f},{:.2f})".format(x,y))