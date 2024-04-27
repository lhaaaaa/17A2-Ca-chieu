# Khởi tạo dictionary
dict1 = {1: 3, 2: 4, 3: 5}
# print(dict1)

# Khởi tạo dictionary rỗng
#dict1 = {}
#dict2 = dict()

# Sử dụng vòng lặp với dictionary
# Lặp qua các key của dictionary
#for key in dict1: #Truy cập vào từng key trong dictionary
#    value = dict1[key] 
#    print(value)

# Lặp qua cặp key-value của dictionary
#for key, value in dict1.items():
#    print(key)
#    print(value)
#    print("-------")

# Các thao tác cơ bản trên dictionary
# Thêm phần tử vào dictionary
# Thêm một phần tử mới (cặp giá trị key-value) vào dictionary
#dict1[4] = 6 #Thêm phần tử mới
#print(dict1)
# Cập nhật giá trị cho key (key này đã tồn tại trong dictionay)
#dict1[4] = 7 #Cập nhật giá trị cho key
#print(dict1)

# Truy xuất giá trị từ key
#print(dict1[2])
#print(dict1.get(3))

# Xóa phần tử từ key
# Sử dụng câu lệnh del
# del dict1

# Sử dụng phương thức pop
# print(dict1.pop(1))
# print(dict1)

# Sử dụng phương thức popitem
# dict1.popitem()
# print(dict1)

# Sử dụng phương thức clear
#dict1.clear()
#print(dict1)

# Lấy danh sách các key và danh sách các value
#print(dict1.keys())
#print(dict1.values())

# Sao chép một dictionary
# Sử dụng phương thức copy
#dict2 = dict1.copy()
#print(dict2)

# Tìm giá trị lớn nhất và giá trị nhỏ nhất trong dictionary
#print(max(dict1))

# Hàm all()
# Giá trị trả về là True khi tất cả các giá trị của khóa là True
# Giá trị trả về là False khi ngược lại
# Một số điều cần lưu ý:
# Các giá trị của khóa có thể là True, 1 hoặc 0
# Dictionary rỗng sẽ trả về giá trị True
"""
dict1 = {"key1": True, "key2": False, "key3": True}
dict2 = {"key1": True, "key2": True, "key3": True}
dict3 = {"key1": False, "key2": False, "key3": False}
dict4 = {}
print(all(dict1.values()))
print(all(dict2.values()))
print(all(dict3.values()))
print(all(dict4))
"""

# Nối 2 dictionary
#dict2 = {1: 3, 2: 4, 3: 5}
#dict3 = {4: 6, 5: 7}
# Sử dụng update
#dict2.update(dict3)
#print(dict2)
#print(dict3)

# Sử dụng toán tử |
#dict2 | dict3
#print(dict2)
#print(dict3)

#dict2 = {x: x**2 for x in range(5)}
#print(dict2)

#list = [1,2,3,4]
#dict3 = {x: x**3 for x in list}
#print(dict3)

