#-----------------------------------------
# Lý thuyết tuple
# Khởi tạo tuple 
#tuple = (1,2,3,4,5)
#print(tuple)
# Khai báo một tuple rỗng
#tuple1 = ()
#tuple2 = tuple()
# Khai báo một tuple gồm 1 phần tử
#tuple1 = (6,)
# Xác định độ dài của một tuple
#print(len(tuple))
# Truy cập vào phần tử trong một tuple
#print(tuple[0])

# Sử dụng vòng lặp với tuple
# Truy cập theo index 
#for index in range(len(tuple)):
#    print(tuple[index], end = " ")
# Truy cập vào phần tử
#print()
#for element in tuple:
#    print(element, end = " ")
# Truy cập vào index và phần tử
#for index, element in enumerate(tuple):
#    print(f"Phần tử ở vị trí {index} có giá trị bằng {element}")

# Truy cập các phần tử trong tuple
# Sử dụng tuple[index] -> truy cập từng phần trong tuple
#print(tuple[2])
# Sử dụng slicing -> truy cập vào từng tuple con trong tuple
#print(tuple[:2])
#print(tuple[2:])
#print(tuple[::-1]) #-Đảo ngược các phần tử trong tuple
# Sử dụng phương thức index -> In ra vị trí của phần tử trong tuple
#print(tuple.index(3))

# Nối các tuple
#tuple1 = (3,4,5,6)
#tuple3 = tuple + tuple1
"""
Đề bài: Khởi tạo một tuple rỗng, đưa các giá trị nhập vào từ bàn phím vào tuple
trống đó và in ra màn hình tuple sau khi có các giá trị trên.

tuple2 = ()
while True:
    a = int(input("Nhập vào một số: "))
    if a == 0:
        break
    tuple2 = tuple2 + (a,)
print(tuple2)
"""

# Đếm số phần tử trong tuple
#print(tuple3.count(5))

# Giá trị lớn nhất và giá trị nhỏ nhất trong tuple
#print(max(tuple1))
#print(min(tuple1))

# ------------------------------------
# Lý thuyết set
# Khai báo và khởi tạo set
#set1 = {1,2,3,4,5}
#print(set1)
# Khởi tạo set trống
#set2 = set()
# Độ dài của một set
#print(len(set1))

# Sử dụng vòng lặp trong set
#for element in set1:
#    print(element, end = " ")

# Các thao tác cơ bản trên set
# Thêm một hoặc nhiều phần tử vào set
# Sử dụng phương thức add 
#set1.add(6)
#print(set1)
# Sử dụng toán tử |=
#set1 |= {7}
#print(set1)
#set1 |= {7,8,9,10}
#print(set1)
# Sử dụng phương thức update
#set1.update({11,12,13})
#print(set1)

# Xóa phần tử khỏi set
# Sử dụng phương thức pop -> Xóa phần tử đầu tiên từ trái sang, phần tử bị lấy vẫn lưu trữ
#a = set1.pop()
#print(a)
#print(set1)

# Sử dụng phương thức remove -> Xóa phần tử được lựa chọn, phần tử bị xóa sẽ không còn trong bộ nhớ
#set1.remove(3)
#print(set1)

# Sử dụng phương thức discard -> gần giống với remove
#set1.discard(4)
#print(set1)
#set1.remove(3)
#set1.discard(3)

# Sử dụng phương thức clear -> xóa mọi phần tử trong set, trả về set rỗng
#set1.clear()
#print(set1)
# Sử dụng del
#del set1
#print(set1)

# Sử dụng toán tử -=
#set1 -= {4}
#print(set1)

# Phép toán hợp của hai hay nhiều tập hợp
#set1 = {1,2,3,4,5}
#set2 = {3,4}
#set3 = {6,7,8,9,10}
#set4 = {2,3,6}
# Sử dụng toán tử |
#union_set = set1 | set2 | set3
#print(union_set)
# Sử dụng phương thức union
#union_set1 = set1.union(set2).union(set3)
#print(union_set1)

# Phép toán giao của hai hay nhiều tập hợp
# Sử dụng toán tử &
#intersection_set = set1 & set2
#print(intersection_set)
# Sử dụng phương thức intersection
#intersection_set1 = set1.intersection(set2)
#print(intersection_set1)
#intersection_set2 = set1.intersection(set3)
#print(intersection_set2)

# Phép toán lấy hiệu hai tập hợp
# Sử dụng toán tử - 
#difference_set = set1 - set2
#print(difference_set)
# Sử dụng phương thức difference
#difference_set1 = set1.difference(set2)
#print(difference_set1)

# Phép toán lấy hiệu đối xứng hai tập hợp
# Sử dụng phương thức symmetric_difference
#hieu_doi_xung = set1.symmetric_difference(set4)
#print(hieu_doi_xung)

#Thay đổi tập hợp dựa trên phép toán tập hợp
# Phương thức .difference_update()
#set1.difference_update(set2)
#print(set1)
# Phương thức .symmetric_difference_update()
#set1.symmetric_difference_update(set2)
#print(set1)
# Phương thức .intersection_update()
#set1.intersection_update(set2)
#print(set1)

# Một số phép toán khác
# isdisjoint -> True khi hai tập hợp là rời nhau (không giao nhau)
#print(set1.isdisjoint(set2))
# issubset -> True khi tập này là con của tập hợp kia
#print(set1.issubset(set2))
# issuperset -> True khi tập này là cha của tập kia
#print(set1.issuperset(set2))

#--------------------------------
# Module collections
# Lớp Counter
"""
from collections import Counter
list_vd = [1, 2, 3, 4, 5, 1, 2, 2, 2, 3]
tuple_vd = (1, 2, 3, 4, 5, 1, 2, 2, 2, 3)
dict1 = Counter(list_vd)
dict3 = Counter(tuple_vd)
print(dict3)
print(dict1)
# Không sử dụng Counter
dict2 = {}
for i in list_vd:
    count = 0
    for j in list_vd:
        if i == j:
            count += 1
    dict2[i] = count
print(dict2)


# Lớp defaultdict
from collections import defaultdict
dict = defaultdict(int)
dict["Hoa"] = 9.5
dict["Bình"] = 5.5
print(dict)
print(dict["An"])

# Lớp deque
from collections import deque
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)
my_list.remove(my_list[0])
print(my_list)

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
print(my_deque)
my_deque.popleft()
print(my_deque)

# Lớp namedtuple
from collections import namedtuple
tp1 = ("Hoa", 15, 7.5)
print(tp1[0])

thongtin = namedtuple("thongtin", ["name", "age", "score"])
tp2 = thongtin("Hoa", 15, 7.5)
print(tp2.name)


# Lớp OrderedDict
from collections import OrderedDict
dict1 = {}
dict1["Hoa"] = 6.5
dict1["Bình"] = 8.0
print(dict1)

dict2 = OrderedDict()
dict2["Hoa"] = 6.5
dict2["Bình"] = 8.0
print(dict2)
"""