"""
Bài 1: 
Nhập từ bàn phím một chuỗi ký tự Str. 
Hãy đếm số các ký tự là số trong chuỗi ký tự Str và in kết quả ra màn hình.

chuoi = input("Nhập vào một chuỗi: ")
count1 = 0
# Sử dụng vòng lặp for bằng chỉ mục
for i in range(len(chuoi)):
    if chuoi[i].isnumeric():
        count1 += 1
print("Số lượng ký tự số trong chuỗi ban đầu là:", count1)
count2 = 0
# Sử dụng vòng lặp for bằng ký tự
for i in chuoi:
    if i.isnumeric():
        count2 +=1 
print("Số lượng ký tự số trong chuỗi ban đầu là:", count2)
"""
"""
Bài 2: 
Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str, 
có bao nhiêu ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi ký tự Str.

chuoi = input("Nhập vào một chuỗi: ")
count = 0
for i in chuoi:
    if i.isnumeric():
        count -= 1
    else:
        for a in range(65, 91):
            if i == chr(a):
                count -= 1
        for b in range(97, 123):
            if i == chr(b):
                count -= 1
    count += 1  
print("Số lượng các ký tự không phải chữ tiếng Anh và số là:", count)
"""

"""
Bài 3: Nhập vào một số tự nhiên n từ bàn phím. 
Viết chương trình chuyển số n từ hệ cơ số 10 sang hệ nhị phân. Kết quả là chuỗi nhị phân.

n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print("Mời nhập lại số")
else:
    chuoi_nhi_phan = ""
    while n > 0:
        phan_du = n % 2 
        chuoi_nhi_phan = str(phan_du) + chuoi_nhi_phan
        n = n//2
    print("Chuỗi chuyển từ hệ thập phân sang hệ nhị phân là:", chuoi_nhi_phan)


Bài 10:
Cho trước chuỗi ký tự nhị phân bao gồm toàn các ký tự 0 và 1. 
Viết chương trình chuyển đổi số nhị phân này sang số thập phân.

so_thap_phan = 0
so_mu = 0
for i in range(len(chuoi_nhi_phan)-1, -1, -1):
    so_thap_phan += int(chuoi_nhi_phan[i])*(2**so_mu)
    so_mu += 1
print("Số thập phân chuyển từ chuỗi nhị phân là:", so_thap_phan)
"""

"""
Bài 4: 
Cho trước 2 chuỗi ký tự Str1, Str2 (nhập vào từ bàn phím). 
Viết chương trình trộn chuỗi ký tự 1 và 2. Việc trộn Str1 và Str2 thực hiện theo quy tắc sau:
+ Lần lượt từ trái sang phải, viết các ký tự của Str1, sau đó đến Str2
+ Nếu một trong hai chuỗi kết thúc thì chỉ viết ra các ký tự của chuỗi còn lại
Input:
Str1 = “abc”
Str2 = “ghiklm”
Output: “agbhciklm”

str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
chuoi_tron = ""
min_length = 0
if len(str1) > len(str2):
    min_length = len(str2)
else:
    min_length = len(str1)

for i in range(min_length):
    chuoi_tron += str1[i] + str2[i]

if len(str1) > len(str2):
    chuoi_tron = chuoi_tron + str1[min_length:]
else:
    chuoi_tron = chuoi_tron + str2[min_length:]

print("Chuỗi trộn của 2 chuỗi trên là:", chuoi_tron)
"""

"""
Bài 5: 
Cho trước (hoặc nhập vào từ bàn phím) chuỗi ký tự Str. 
Hãy xóa đi tất cả các ký tự Str không phải là số, chuỗi ký tự còn lại sẽ là số. 
In ra kết quả chuỗi số này và thông báo cho biết chuỗi đó có phải là số hoàn hảo không.

chuoi = input("Nhập chuỗi từ bàn phím: ")
# Thay thế ký tự không phải là số bằng ""
chuoi1 = chuoi
chuoi2 = ""
for i in chuoi1:
    if i.isnumeric() == False:
        chuoi1 = chuoi1.replace(i,"")
# Tạo một chuỗi mới chỉ gồm các số
for i in chuoi:
    if i.isnumeric():
        chuoi2 += i
print(chuoi1)
print(chuoi2)

# Kiểm tra chuỗi đó có phải số hoàn hảo không
a = int(chuoi1)
sum = 0
for i in range(1,a):
    if a % i == 0:
        sum += i
if a == sum:
    print("Chuỗi số đã tách từ chuỗi ban đầu là số hoàn hảo")
"""

"""
Bài 7: 
Cho trước xâu Str là một đoạn văn bản hoàn chỉnh (có thể bao gồm nhiều dòng). 
Nhập vào một từ đơn, hãy tìm trong chuỗi ký tự Str xem chứa bao nhiêu từ đơn này

van_ban = '''
Cả hai mô hình, LR và XGB, có cùng mức độ trung bình của AUC (diện tích 
dưới đường cong ROC), tức là hiệu suất của chúng trong việc dự đoán thu nhập
cá nhân là tương đương. Tuy nhiên, mô hình XGB có khoảng tin cậy hẹp hơn,
điều này tức là kết quả của nó có độ chính xác cao hơn và không dao động nhiều.
Khi phân tích đường cong ROC, chúng ta nhận thấy rằng mô hình XGB có hiệu
suất tốt hơn một chút trong việc dự đoán thu nhập cao trong tất cả các nhóm
đo lường. Điều này có nghĩa là mô hình XGB đưa ra dự đoán chính xác hơn khi
xác định các cá nhân có thu nhập cao. Trong khi đó, mô hình LR lại cho kết quả
tốt hơn trong việc dự đoán thu nhập trung bình.
'''
tu_don = input("Nhập vào từ đơn cần tìm trong đoạn văn: ")

# Sử dụng count
a = van_ban.count(tu_don)
print(f"Số lượng từ '{tu_don}' trong đoạn văn bản trên là {a}.")
"""


