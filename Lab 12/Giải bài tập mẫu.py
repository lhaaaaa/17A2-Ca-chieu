"""
Bài 1:
Viết một chương trình yêu cầu nhập một số nguyên từ bàn phím, 
trong đó xử dụng bẫy lỗi. Nếu người dùng nhập không đúng kiểu số 
nguyên chương trình sẽ liên tục ra thông báo "Bạn cần nhập vào một 
số nguyên!" cho đến khi người dùng nhập đúng.

while True:
    try:
        n = int(input("Nhập vào một số nguyên: "))
        print(n)
        break
    except ValueError as e:
        print("Lỗi: Bạn cần nhập vào một số nguyên!")
"""

"""
Bài 2:
Cho một file chương trình 12.2_a.py có nội dung sau đây:
Thực hiện các yêu cầu sau:
b) Xử dụng xử lý ngoại lệ để khắc phục lỗi của đoạn mã trên.

lst = [1,2,3,4,5]
i = 0
sum = 0
while True:
    try:
        sum = sum + lst[i]
        i += 1
    except KeyboardInterrupt:
        print("Đã dừng vòng lặp")
    except Exception as e:
        print("Đã xảy ra lỗi: ", e)
        break
print("Tổng dãy số đã cho là:", sum)
"""

"""
Bài 4:
Hàm Sinh_list(n) với n có thể nhập từ bàn phím có chức năng yêu cầu 
người dùng nhập và trả về danh sách list có n phần tử là số tự nhiên. 
Hãy viết hàm số này với yêu cầu bắt lỗi Exception chính xác.

def sinh_list(n):
    lst = []
    try:
        for i in range(n):
            a = int(input("Nhập vào số tự nhiên: "))
            lst.append(a)
        return lst
    except Exception as e:
        print("Xảy ra lỗi:", e)

n = int(input("Nhập số phần tử của lst: "))
print(sinh_list(n))
"""

"""
Bài 5:
Viết lại chương trình sử dụng hàm để thực hiện phép chia hai số nguyên. 
Nếu người dùng nhập mẫu số bằng 0, hàm sẽ kích hoạt một lệnh assert và 
bắt lỗi ngoại lệ với thông báo "Cannot divide by zero". Chương trình 
sẽ in ra thông báo lỗi "Lỗi: Cannot divide by zero” nếu lỗi được bắt. 
Nếu người dùng nhập không phải là số nguyên, chương trình sẽ in ra thông 
báo “Bạn phải nhập số nguyên”. Nếu có lỗi khác xảy ra, chương trình sẽ 
in ra thông báo “Đã có lỗi xảy ra”.

while True:
    try:
        a, b = map(int, input("Nhập vào số bị chia và số chia: ").split())
        assert b != 0, "Số chia phải khác 0"
        ket_qua = a/b
        print("Kết quả:", ket_qua)
        break
    except Exception as e:
        print("Lỗi chương trình: ", e)
        break
"""
