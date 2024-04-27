"""
Bài 8: 
a) Viết chương trình sử dụng dictionary lưu các thông tin về tivi bao gồm 
(Hãng, model, năm sản xuất). In nội dung thông tin ra màn hình.
b) Giả sửa dictionary lưu các thông tin khóa (key) về tivi bao gồm (Hãng, 
model, năm sản xuất). Viết chương trình kiểm tra một key có tồn tại trong 
từ điển không?

dict1 = {"tivi1": {"hang": "LG", "model": "ABC", "namsx": 2020}, 
         "tivi2": {"hang": "Sony", "model": "DEF", "namsx": 2021}}
print(dict1)

if "tivi3" in dict1:
    print("Có dữ liệu về tivi 3 trong dictionary")
else:
    print("Không có dữ liệu về tivi 3 trong dictionary")
"""

"""
Bài 10:
Một từ điển D được định nghĩa bao gồm Khóa là mã sinh viên trong lớp, 
value là cặp 3 giá trị tên, điểm HP1, điểm HP2. 
Ví dụ: D=("K1701":|" Hà', 7,9.5), "K1702": [Bình',10,8], "K1703":[Hoa, 6.0,91}
Viết chương trình nhập bộ dữ liệu từ điển trên như sau:
+ Đầu tiên yêu cầu người dùng nhập mã sinh viên.
+ Tiếp theo yêu cầu nhập, tên, điểm HP1 và điểm HP2 trên một dòng bởi 1 chuỗi ký tự, và 2 số, cách nhau bởi dâu phấy.
+ Thông báo loại 1: "Đã hoàn thành nhập điểm cho sinh viên mới.”
+ Thông báo loại 2: "Đã hoàn thành cập nhật lại nhập điểm cho sinh viên trong danh sách."
Bài 11:
Cho trước bộ dữ liệu điểm các học phần 1, học phần 2 và học phần 3 của các sinh viên lớp K17.
Ví dụ: D=("K1701": ['"Hà, 7,9.5], "K1702" ['Bình',10,81}
Viết chương trình tính điểm trung bình của K17 và in ra màn hình nội dung như sau:
Điểm trung bình: 
K1701
Hà: 8.25
K1702
Bình: 9.0

dict1 = {}
while True:
    ma_sv = input("Nhập mã sinh viên: ")
    thong_tin_sv = []
    if ma_sv == "0":
        break
    ten_sv, diem_hp1, diem_hp2, diem_hp3 = map(str, input("Nhập các thông tin của sinh viên: ").split(","))
    thong_tin_sv.append(ten_sv)
    thong_tin_sv.append(diem_hp1)
    thong_tin_sv.append(diem_hp2)
    thong_tin_sv.append(diem_hp3)
    dict1[ma_sv] = thong_tin_sv
print(dict1)
for key in dict1:
    tong = 0
    ten_sv = dict1[key].pop(0)
    diem_sinh_vien = dict1[key]
    for diem in diem_sinh_vien:
        tong += float(diem)
    diem_trung_binh = round(tong/(len(diem_sinh_vien)),2)
    print(f"Điểm trung bình của sinh viên {ten_sv} có mã sinh viên là {key} là {diem_trung_binh}")
"""

"""
Bài 12:
Cho trước một đoạn mã văn bản tiếng Anh:
Str = " Glucose is the fundamental thing that burns energy in our bodies. 
We get glucose from the foods we eat and it is transmitted to all cells via 
blood. This way, glucose ensures the energy which the cell needs. The quantity 
of the glucose in our blood shows us some data about our body's health. 
Measuring blood glucose level is the most common way to control people's 
medical condition."
Viết chương trình đếm xem đoạn văn bản trên có bao nhiêu từ và 
tần suất xuất hiện các từ trong chuỗi Str.
"""
text = """
Glucose is the fundamental thing that burns energy in our bodies. 
We get glucose from the foods we eat and it is transmitted to all cells via 
blood. This way, glucose ensures the energy which the cell needs. The quantity 
of the glucose in our blood shows us some data about our body's health. 
Measuring blood glucose level is the most common way to control people's 
medical condition.
"""
# Loại bỏ các dấu chấm câu
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("'s", "")
text = text.lower()
print(text)
word_list = text.split()
dict1 = {}
for i in word_list:
    count = 0
    for j in word_list:
        if i == j:
            count += 1
    dict1[i] = count
print(dict1)
