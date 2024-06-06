# Câu lệnh try except
"""
try:
    ket_qua = 10/2
    print(ket_qua)
except ZeroDivisionError:
    print("Error", ZeroDivisionError)
"""

# Câu lệnh try except finally
"""
try:
    ket_qua = 10/0
except ZeroDivisionError as e:
    print(f"Error:", e)
finally:
    print("Câu lệnh luôn thực thi")
"""

# Câu lệnh try except else
"""
try:
    ket_qua = 10/0
except ZeroDivisionError as e:
    print(f"Error:", e)
else:
    print("Câu lệnh luôn thực thi")
"""

#Xử lý nhiều ngoại lệ
"""
try:
    ket_qua = a
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError as e:
    print("Error:", e)
except Exception as e:
    print("Ngoại lệ thông thường:", e)
"""

# Gộp nhiều ngoại lệ vào chung một except
"""
try:
    ket_qua = 10/0
except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("Error:", e)
    elif isinstance(e, ZeroDivisionError):
         print("Error:", e)
    else:
        print("Ngoại lệ thông thường:", e)
"""

# Câu lệnh assert:
"""
def divide(a, b):
    assert b != 0, "Đây là số không, nên không chia được"
    return a/b

print(divide(10, 2))
print(divide(10, 0))
"""
# raise
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Đây là số 0, nên không chia được")
    return a/b
try:
    ket_qua = divide(10,0)
    print(ket_qua)
except ZeroDivisionError as e:
    print(e)
