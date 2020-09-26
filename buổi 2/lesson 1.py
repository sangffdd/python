#in n lần hello python
n= int(input('nhap n= ' ))
for n in range (0,n,1):
    print("hello word")
#tính tổng từ 1 đến n
n= int(input('nhap n= '))
sum = 0
for i in range (1,n+1):
    sum += i
print("Tong tu 1 den", n ,"la: ", sum )
#tính tổng số chẵn nằm trong đoạn từ 0 đến n
n= int(input('nhap n = '))
chan=0
for i in range (0,n+1):
    if( i % 2 ==0 ):
        chan += i
        print (i)  
    else:
        print()
print("tong cac so chan ", chan)
#4.	Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
n =int(input('nhap n= '))
le=0
for i in range (0,n+1):
    if(i % 2 !=0 ):
        le +=i
        print (i)
    else:
        print()
print("tong cac so le ", le)
#5.	Tính trung bình cộng các số trong mảng
n = int(input('nhap n= '))
tong=0
i=1
tongtrungbinh = int
for i in range(i,n+1):
    tong +=i
    print (tong)
tongtrungbinh = tong / n
print("tong trung binh cong trong mang ", tongtrungbinh)
#6.	Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
n = int(input('nhap n= '))
tong = 0
for i in range (1,n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)
#7.	Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
n= int(input('nhap n= '))
tong= 0
for i in range (1,n+1):
    if(i == 17):
        continue
         
    else:
        tong += i
        print(i, tong)
print (tong)
#bài tập về nhà 1
from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
#3 bài tập về nhà
n = int(input("nhap n= "))
total = 0
while (n):
    if(n>100):
        print("nhap lai n") 
        break
    if(n<100):
        while (n):
            total = total + n % 10
            n = int(n / 10)

print(total)
#4 bài tập về nhà
from math import sqrt
a=int(input("nhap a= "))
b=int(input("nhap b= "))
c=int(input("nhap c= "))
if( (a<b+c)&(b<a+c)&(c<a+b) ):
    if( (a*a==b*b+c*c) | (b*b==a*a+c*c) | (c*c== a*a+b*b)):
        print("đây là hình tam giác vuông")
    else:
       print("đây là hình tam giác nhưng không phải là hình tam giác vuông")
else:
    print("đây không phải hình tam giác")