"""
Bài 1: 
Viết chương trình nhập a, b, c là độ dài 3 cạnh một tam giác, 
tính diện tích tam giác đó. Chương trình xử lý ngoại lệ trong các 
tình huống sau:
+ Người dùng nhập a, b, hoặc c không phải là kiểu số.
+ Người dùng nhập giá trị 0 hoặc số âm cho a, b hoặc c.
+ Người dùng nhập a, b, c dương nhưng không thóa mẫn điều kiện tồn 
tại tam giác.

def dien_tich_tam_giac(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        raise ValueError("Các cạnh phải là số nguyên")
    
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Các cạnh phải lớn hơn 0")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Các cạnh không tạo thành tam giác")   
     
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

a, b, c = map(int, input("Nhập 3 cạnh của tam giác: ").split())
try:
    print(dien_tich_tam_giac(a,b,c))
except ValueError as e:
    print(e)
"""

"""
Bài 2: 
Viết chương trình cho phép người dùng nhập một chuỗi ký tự từ bàn phím:
+ Việc nhập liệu kết thúc bình thường (không exception) khi người dùng 
nhập vào các ký tự a,b...z hoặc A,C,...Z.
+ Phát sinh exception và thông báo lỗi "Lỗi ký tự !!!" khi người dùng 
nhập vào một phím không phải là ký tự. 
+ Phát sinh exception và thông báo lỗi "Lỗi nhập liệu !!!" khi người 
dùng nhập vào một chuỗi có 2 ký tự liên tiếp giống nhau.
+ Phát sinh exception và thông báo lỗi "Lỗi nhập lặp lại !!!" khi người 
dùng nhập vào 4 ký tự liên tiếp giống nhau.
+ Phát sinh exception và thông báo lỗi "Lỗi nhập trùng lặp !!!" khi người
 dùng nhập vào 5 từ giống nhau liên tiếp.
+ Sau khi phát sinh exception, xử lý và thông báo, chương trình lại tiếp 
tục hoạt động bình thường.

def kiem_tra_chuoi(chuoi):
    if not all(c.isalpha() for c in chuoi):
        raise ValueError("Chuỗi chỉ được chứa các ký tự chữ")
    
    for i in range(len(chuoi) - 4): #5 ký tự trùng lặp
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] == chuoi[i+4]:
            raise ValueError("Lỗi nhập trùng lặp !!!")
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]: #4 ký tự trùng lặp
             raise ValueError("Lỗi nhập lặp lại !!!") 
    for i in range(len(chuoi) - 1): # 2 ký tự trùng lặp
        if chuoi[i] == chuoi[i+1]:
            raise ValueError("Lỗi nhập liệu !!!")
        
str = input("Nhập vào một chuỗi để kiểm tra: ")
try:
    print(kiem_tra_chuoi(str))
except ValueError as e:
    print(e)
"""

"""
Bài 5: 
Cho các tổng sau:
S1=1+2+...+ n.
S2=1+2^2+ 3^2 + ….+ n^2
Viết chương trình (sử dụng kỹ thuật đệ qui) để tính các tổng trên với 
n được nhập từ bàn phím. Chương trình được sử dụng kỹ thuật bắt lỗi và 
raise để đưa ra thông báo lỗi trong các trường hợp. Người dùng nhập sai 
n là một giá trị không hợp lệ hoặc gây ra lỗi tính toán, chương trình sẽ 
đưa ra thông báo lỗi tương ứng. 
Nếu không có lỗi xảy ra, chương trình sẽ tính toán và in ra kết quả.

def sum_to_n(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n phải là số nguyên dương")
    if n == 1:
        return 1
    else:
        try:
            return n + sum_to_n(n-1)
        except OverflowError:
            raise OverflowError(f"Tổng các số từ 1 đến {n} vượt quá giới hạn")

n = int(input("Nhập vào một số nguyên dương: "))
try:
    print(sum_to_n(n))
except (ValueError, OverflowError) as e:
    print(e)
 
def sum_square_to_n(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n phải là số nguyên dương")
    if n == 1:
        return 1
    else:
        try:
            return n**2 + sum_square_to_n(n-1)
        except OverflowError:
            raise OverflowError(f"Tổng các số từ 1 đến {n} vượt quá giới hạn")

n = int(input("Nhập vào một số nguyên dương: "))
try:
    print(sum_square_to_n(n))
except (ValueError, OverflowError) as e:
    print(e)
"""  

"""
Bài 6: 
Giả sử rằng địa chỉ email của công ty có dạng username@companyname.com, 
hãy viết một chương trình để nhập vào địa chỉ email của nhân viên biết 
rằng dữ liệu nhập vào là chuỗi ký tự str đại diện cho username, 
chương trình sẽ tự động ghép thành tổng chuỗi str +"@companyname.com' 
và lưu vào một danh sách.
Biết rằng: Tên nhân viên không được có dấu cách và chỉ bao gồm chữ số 
(0,1,2...9) và chữ cái thường trong tập hợp (a,b,...z) và chữ cái hoa 
(A,B,...Z). Sử dụng xử lý ngoại lệ để đưa ra thông báo lỗi mỗi khi nhập 
sai username.


def tao_email(username):
    for c in username:
        if c in "~`@#$%^&*()_+={}[]:;<>?/" or c.isspace():
            raise ValueError("Username không được chứa ký tự khác và dấu cách")
    email = username + "@companyname.com"
    return email
lst_email = []
while True:
    try:
        username = input("Nhập vào username: ")
        email = tao_email(username)
        print(email)
        lst_email.append(email)
    except ValueError as e:
        print(e)
        break
print("List email:", lst_email)
"""
