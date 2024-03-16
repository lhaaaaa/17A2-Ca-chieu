#Bài 1
#retained = 100
#interest = 0.15
#tong_tien = retained * ((1 + 0.15)**10)
#print("Tổng tiền có được sau 10 năm là {:.2f}".format(tong_tien))

#Bài 3
"""
print(
Shall I compare thee to a summer's day?
Thou art more lovely and more temperate: 
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:
	Sometime too hot the eye of heaven shines,
	And often is his gold complexion dimmed;
	And every fair from fair sometime declines,
	By chance or nature's changing course untrimmed;
But thy eternal summer shall not fade
Nor lose possession of that fair thou owest;
Nor shall Death brag thou wanderest in his shade,
When in eternal lines to time thou growest:
	So long as men can breathe or eyes can see,
	So long lives this, and this gives life to thee.
(Sonnet 18 by William Shakespeare )
)
"""

#Bài 4
#a = float(input("Nhập độ C:"))
#b = a + 273.15
#print("Nhiệt độ K là:", b)

#Bài 5
#m,n = map(int, input("Nhập 2 số nguyên dương:").split())
#print("Giá trị phần dư là", m%n)
#print("Giá trị phần nguyên là", m//n)

#Bài 6
import math 
#r = float(input("Nhập bán kính:"))
#s = math.pi *r*r
#print("Diện tích hình tròn là: {:.2f}".format(s))

#Bài 7
#h = float(input("Nhập độ cao:"))
#g = 9.8 #m/s^2
#v1 = (2*g*h)**0.5
#v2 = math.sqrt(2*g*h)
#print("Vận tốc rơi tự do 1 là:{:.2f}".format(v1))
#print("Vận tốc rơi tự do 2 là:", v2)

#Bài 8
#a,b,h =map(float, input("Nhập vào các số đo").split())
#s = (a + b) *h /2
#print("Diện tích hình thang là:", s)

#Bài 9
#a, b, c = map(int, input("Nhập độ dài 3 cạnh của tam giác").split())
#d = a + b + c
#p = d/2 
#s =(p*(p-a)*(p-b)*(p-c))**0.5
#print("Chu vi và diện tích của tam giác lần lượt là {} và {}".format(d, s))

#Bài 10
#x, y = map(float, input("Nhập 2 giá trị x, y").split())
#tu = math.sin(x)
#mau = (2*x+y)/math.cos(x) - x**y/(x-y)
#f_x_y = tu/mau
#print("Giá trị biểu thức là", f_x_y)