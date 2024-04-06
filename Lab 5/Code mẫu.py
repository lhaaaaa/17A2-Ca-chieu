# Định nghĩa về chuỗi
#a = "Hello 1234"
#print(a)
#print(type(a))

# Truy cập giá trị trong chuỗi
# Truy cập từng ký tự trong chuỗi bằng chỉ mục dương, từ trái sang phải
    #a = "Khoa hoc du lieu"
    #print(a[3])
# Truy cập từng ký tự trong chuỗi bằng chỉ mục âm, từ phải sang trái
    #a = "adgjdniwgj oedgjnkw9184 p4529 *((*^^*()))nfi  nfiwefjpwt55542267hy553248"
    #print(a[-2])
# Truy cập bằng slicing
"""
a = "Khoa hoc du lieu"
print(a[1:4:2]) # [start:end:step]
print(a[1:4]) # [start:end]
print(a[:4]) # [:end] -> Khuyết start, chuỗi sẽ cắt từ đầu tới chỉ mục end - 1 
print(a[4:]) # [start:] -> Khuyết end, chuỗi sẽ cắt từ chỉ mục số 4 tới cuối chuỗi
print(a[::]) # -> Khuyết cả 3, chuỗi là chuỗi ban đầu
print(a[::-1]) # -> Chuỗi đảo ngược
"""

# Chiều dài chuỗi 
"""
a = "Hello"
print(len(a))
# Sử dụng vòng lặp for bằng cách dùng chỉ mục:
for i in range(len(a)):
    print(a[i], end = " ")
# Sử dụng vòng lặp for bằng ký tự:
print()
for i in a:
    print(i, end = " ")
"""

# Các hàm xử lý cơ bản trong chuỗi
#a = "Hello"
# lower() -> chuyển in hoa thành in thường
#print(a.lower())
# upper() -> chuyển in thường thành in hoa
#print(a.upper())
# strip()
#b = "         fhwe  tj391 1939          "
#print(b.strip())
# split(ký tự phân cách)
#e = "Hello,1234"
#print(e.split(","))
# replace(ký tự cũ, ký tự mới)
#print(a.replace("l", "n"))
# find(ký tự)
#print(a.find("l"))
#print(a.find("3"))
# rfind(chuỗi ký tự con)
#a = "Khoa hoc du lieu"
#print(a.rfind("hoc"))
# count(ký tự tự chọn)
#print(a.count("o"))
# isdigit
#b = "abc"
#print(b.isdigit())
#print(b.isnumeric())
#print(b.isalpha())
# capitalize()
#a = "hellO"
#print(a.capitalize())

#Nối chuỗi
str1 = "abc"
str2 = "123"
print(str1 + str2)
print(str1 + " " + str2)
