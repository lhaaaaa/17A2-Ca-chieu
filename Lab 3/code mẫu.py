# Hàm range(start, stop, step)
range(1,7,1) 
#-> Tạo ra một chuỗi số bắt đầu từ 1 và kết thúc 6, bước nhảy 1. Chuỗi số gồm: 1,2,3,4,5,6
range(8) 
#-> Tạo ra một chuỗi số bắt đầu từ 0 và kết thúc 7, bước nhảy 1. Chuỗi số gồm: 0,1,2,3,4,5,6,7
# range(8,5) sai -> Giá trị bắt đầu luôn phải nhỏ hơn hoặc bằng giá trị kết thúc
# Trừ phi
range(8,5, -1) 
# -> Tạo ra một chuỗi số GIẢM bắt đầu từ 8 và kết thúc ở 4, bước nhảy -1. CHuỗi số gồm: 8,7,6,5,4
range(1,1)
# -> Tạo ra một chuỗi số rỗng

# range(1.5, 8) sai -> Tất cả tham số trong hàm range() phải là số nguyên

# Vòng lặp for
#for i in range(5):
#    print(i)
#print("Hello")
"""
Cách hoạt động:
Bước 1: Vòng lặp for bắt đầu hoạt động. Biến chạy i bắt đầu chạy từ 0 đến 4, bước nhảy 1
Bước 2: Thực hiện vòng lặp:
i = 0 -> Thực hiện lệnh in giá trị i -> In ra 0
i = 1 -> Thực hiện lệnh in giá trị i -> In ra 1
i = 2 -> Thực hiện lệnh in giá trị i -> In ra 2
i = 3 -> Thực hiện lệnh in giá trị i -> In ra 3
i = 4 -> Thực hiện lệnh in giá trị i -> In ra 4
Bước 3: Dừng vòng lặp
"""
for i in range(5):
    print(j)

