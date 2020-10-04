# mẫu
# def < tên hàm > (tham số truyền vào ) 
def xinchao():
    print("chao cac ban sv vd")
xinchao()
#1 tìm số đảo của số n
print("Bài 1: ")
n = str(input("nhap n= "))
print(str(n)[::-1])
#2 tìm n!
n = int(input("nhap n= "))
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thua của ",n," là ",tinhgiaithua(n))
#3 tính tổng 1^3 2^3 n^3
n = int(input("nhap n= "))
s=0
for i in range (1,n+1):
    s= s + pow(i,3)
    print(s)
#4 tính tổng các số lẻ
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 != 0):
            s+=i
    print("tổng các số lẻ là: ", s)
    return 

n=int(input("nhap n= "))
print(tong(n))
#5 tính tổng các số chẵn
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 == 0):
            s+=i
    print("tổng các số chẵn là: ", s)
    return 

n=int(input("nhap n= "))
print(tong(n))
#6 xem 1 số có phải số nguyên tố hay không 
def songuyento(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "là số nguyên tố"
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print(songuyento(n))
#7 xem 1 số có phải số chính phương hay không
import math
n=int(input("nhap n= "))
x = math.sqrt(n)
def sochingphuong(n):
    if(x * x == n):
        return "là số chính phương"
    else:
        return  "không phải là số chính phương"
print(n,sochingphuong(n))
#8 tính tổng các số nguyên tố từ 1 đến n
def songuyento(n):
    count = 0
    s =0 
    for i in range(1, n + 1):
        if n % i == 0:
            s=s+i
            count += 1
    if count == 2:
        return s
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print("tong cac so nguyen to la: ",songuyento(n))
#9 in ra bảng cửu chương n
#in ra bảng cửu chương n 
n= int(input("nhap n= "))
def bangcuuchuong(n):

    for j in range(1,10):
        s = n * j
        print(n, "*" ,j, "=" ,s)
    return s
print(bangcuuchuong(n))
#10 tính số fibo thứ n
def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input("nhap n = "))
print(fibonacci(n))

