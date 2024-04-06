"""
Bài 2:
Cho xâu S, hãy tạo xâu S’ là nghịch đảo của S
Ví dụ: S = “TAN” thì S’ = “NAT”

str1 = "TAN"
str2 = str1[::-1]
print("Chuỗi ban đầu là:", str1)
print("Chuỗi sau khi đảo ngược là:", str2)
"""

"""
Bài 4:
Cho một xâu ký tự chỉ gồm các ký tự “(“ và “)”. 
Hãy kiểm tra xem xâu ký tự đó có là một biểu thức đúng hay không. 
Biết rằng các biểu thức đúng có dạng sau: (), (biểu thức đúng), (biểu thức sai, )abc(

chuoi = input("Nhập vào một chuỗi ký tự để kiểm tra: ")
if chuoi[0] == "(" and chuoi[-1] == ")":
    print("Đây là biểu thức đúng")
else:
    print("Đây là biểu thức sai")
"""

"""
Bài 5:
Cho hai xâu ký tự S1, S2. 
Hãy kiểm tra xem có thể xóa đi một số các ký tự của xâu S1 thì ta được xâu S2 hay không?
str1 = afbgch 
str2 = abc
"""
'''
str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")

str1_xoa = ""
for i in str1:
    for j in str2:
        if i == j:
            str1_xoa = str1_xoa + i
print("Chuỗi 1 sau khi xóa bớt một số phần tử để được chuỗi 2 là:", str1_xoa)

#? Xóa bao nhiêu phần tử?
count = 0 
for i in str1:
    for j in str2:
        if i == j:
            count += 1 
print(f"Chuỗi 1 sau khi xóa bớt {count} phần tử sẽ được chuỗi 2")
'''

"""
Bài 6:
Cho họ và tên một sinh viên. Hãy trích ra tên của sinh viên đó.
Ví dụ S = “Nguyễn Văn Minh”, in ra màn hình “Tên sinh viên: Minh”

hoten_sv = input("Nhập họ tên của sinh viên: ")
ten = ""
for i in range(len(hoten_sv)-1, -1, -1):
    if hoten_sv[i] == " ":
        break
    ten += hoten_sv[i]
dao_nguoc_ten = ten[::-1]
print("Tên sinh viên:", dao_nguoc_ten)
"""

"""
Bài 8: 
Nhập vào một chuỗi ký tự có độ dài 10 ký tự (lẫn cả chữ cái và chữ số). 
Thực hiện các yêu cầu sau:
a) Trích ra chuỗi ký tự con từ vị trí thứ 3 đến vị trí thứ 7
b) Trích ra chuỗi ký tự con gồm 06 vị trí kể từ vị trí đầu tiên
c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 4 ký tự 
d) Đảo ngược chuỗi ký tự nhập vào
"""

chuoi_ky_tu = input("Nhập vào chuỗi ký tự có độ dài là 10 ký tự: ")
if len(chuoi_ky_tu) < 10:
    print("Nhập lại chuỗi ký tự")
else:
    str1 = chuoi_ky_tu[3:8]
    print("Câu a:", str1)
    str2 = chuoi_ky_tu[:6]
    print("Câu b:", str2)
    str3 = chuoi_ky_tu[-1:-5:-1]
    print("Câu c:", str3[::-1])
    str4 = chuoi_ky_tu[::-1]
    print("Câu d:", str4)