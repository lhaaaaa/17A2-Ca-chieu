#Không sử dụng with
"""
file = open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r")
print(file.mode)
file.close()
print(file.closed)
"""
#Sử dụng with
"""
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r") as file:
    print(file.mode)
print(file.closed)
"""
# Đọc dữ liệu trong tập tin
# Sử dụng phương thức read
"""
+ Đọc và trả về toàn bộ nội dung của file dưới dạng một chuỗi
+ Nhược điểm: chuỗi quá lớn nếu nội dung dài
"""
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r") as file:
    content = file.read()
    print(content)

# Sử dụng phương thức readline
"""
+ Đọc và trả về nội dung của từng dòng
+ Nhược điểm: gọi nhiều câu lệnh

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r") as file:
    line1 = file.readline()
    print(line1)
"""
"""
Sử dụng vòng lặp for để in ra dòng cụ thể nào đó

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r") as file:
    for i in range(1):
        file.readline() #Bỏ qua số dòng mong muốn
    line2 = file.readline()
    print(line2)
"""
# Sử dụng phương thức readlines
"""
+ Đọc và trả về nội dung của tất cả các dòng
+ Trả về một danh sách các chuỗi

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/filetest.txt", "r") as file:
    all_line = file.readlines()
    print(all_line[-1])
"""    

#Ghi dữ liệu vào trong tập tin
# Sử dụng phương thức write
"""
+ Ghi mọt chuỗi ký tự vào file
+ Mỗi lần gọi nó sẽ ghi chuỗi ký tự được truyền vào trong phương thức

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/write.txt", "w", encoding= "utf-8") as file:
    file.write("Đây là câu lệnh số 1 \n")
    file.write("Đây là câu lệnh số 2")
"""
# Sử dụng phương thức writelines
"""
+ Ghi một chuỗi các chuỗi ký tự vào file
+ Mỗi chuỗi ký tự đượn đưa vài dòng riêng biệt

with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/writelines.txt", "w", encoding= "utf-8") as file1:
    lines = ["Đây là câu lệnh số 1 \n", "Đây là câu lệnh số 2"]
    file1.writelines(lines)
"""
# Thao tác với file csv
# Đọc dữ liệu trong file csv
import csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/email.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
# Ghi dữ liệu vào trong file csv
with open("C:/Users/ADMIN/OneDrive/Documents/Downloads/Bài giảng thực tập lập trình cơ bản/17A2-Ca-chieu/Lab 11/email2.csv", "w") as file2:
    write = csv.writer(file2)
    write.writerows(data1)