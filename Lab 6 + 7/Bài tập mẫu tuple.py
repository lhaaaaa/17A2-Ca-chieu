"""
Bài 9: 
Cho trước một tuple chứa các số tự nhiên sau (1,2,3,4,5,6,7,8,9,10,11). 
Viết chương trình lưu nửa đầu và nửa cuối của tuple trên vào các tuple 
tp1 và tp2. In kết quả ra màn hình.

tuple = (1,2,3,4,5,6,7,8,9,10,11)
vi_tri_chinh_giua = int(len(tuple)/2) + 1
tp1 = tuple[:vi_tri_chinh_giua]
print(tp1)
tp2 = tuple[vi_tri_chinh_giua:]
print(tp2)
"""

"""
Bài 10: 
Viết chương trình tạo một tuple chứa toàn các số lẻ được lọc ra từ tuple cho trước 
tp = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 

tp = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 
tp_le = ()
for element in tp:
    if element % 2 != 0:
        tp_le = tp_le + (element,)
print(tp_le)
"""