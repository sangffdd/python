#Bai tap 1: Max and Min
print('**********************************')
print('Bai tap 1: Max_Min')
b=int(input('Nhap 1 so B bat ki: '))
a=[3,4,1,8,23,16,18,98,b]
lon = 0
nho = b
for i in a:
    if i < nho:
        nho=i
for i in a:
    if i > lon:
        lon=i
print(lon,' La so Max')
print(nho,' La so Min')
#Bai tap 2: Dao chu
print('**********************************')
print("Bài 2: ")

n= str(input("nhap vao mot chuoi bat ki "))
def reverse_string(n):
    return(str(n)[::-1])
print(reverse_string(n))
#Bai tap 3: SO hoan hao
print('**********************************')
n=int(input("nhap n="))
def is_perfect(n):
    Tong=0
    for i in range (1,n):
        if n % i == 0:
            Tong=Tong+i
    if Tong==n:
        return "là số hoàn hảo"
    else:
        return "không phải là số hoàn hảo"
print(n,is_perfect(n))
#Bai tap 4: So nguyen to
print('**********************************')
print('Bai tap 4: So nguyen to')
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return ' La so nguyen to'
    return ' Khong phai so nguyen to'

n = int(input('Nhap vao so n = ' ))
print(n,is_prime(n))
#Bai tap 5: Chu viet hoa, Chu viet thuong
print('**********************************')
print('Bai tap 5: So luong chu hoa va chu thuong')
def count_upper_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
    print("Cau tu da nhap la: ",s)
    print("So chu in hoa: ", count_upper)
    print("So chu in thuong: ", count_lower)


s = str(input('Viet 1 cau tu: '))
count_upper_lower(s)
#Bai tap 6: Pangram
print('**********************************')
import string
gram = str(input("nhap mot chuoi bat kì"))
def is_pangram (gram):
       gram = gram.lower()
       gram_list_old = sorted([c for c in gram if c != ' '])
       gram_list = []
       for c in gram_list_old:
           if c not in gram_list:
               gram_list.append(c)
       if gram_list == list(string.ascii_lowercase): return True
       else: return False
print(is_pangram(gram))
#Bai tap 7: Matrix
print('**********************************')
import math
n=int(input("nhap n= "))
s=0
tongcacsole=0
while (n):
    s =  n % 10
    if(s % 2 != 0):
        tongcacsole=tongcacsole + 1
    n = int(n / 10)
print("so luong so le la: ",tongcacsole)
#Bài tập 8
m=float(input("nhap vao can nang cua ban: "))
h=float(input("nhap vao chieu cao cua ban: "))
s=float
s1=float
def body_mass_index (m,h):
    s=m/(h*h)
    print("chi so BMI cua ban la",s)
body_mass_index(m,h)

def bmi_information(m,h):
    s1=m/(h*h)
    if(s1 < 18):
        print("ban la nguoi gay")
    elif (s1 <= 29.4):
        print("ban la nguoi binh thuong")
    elif (s1 <= 34.9):
        print("ban bi beo phi cap do II")
    elif (s1 <= 34.9):
        print("ban la nguoi beo pho cap do II")
    else:
        print("ban la nguoi beo phi cap do III")
bmi_information(m,h)
#Bai tap 9: Doi hoa va thuong cho nhau
print('**********************************')
s = str(input('Nhap chu vao : '))
def count_upper_lower(s):
    print(s.upper())
count_upper_lower(s)
#Bài tập 10
import math
n=int(input("nhap n= "))
def tongcacsole(n):
    s=0
    count=0
    while (n):
        s =  n % 10
        if(s % 2 != 0):
            count=count + 1
        n = int(n / 10)
    print("so luong so le la: ",count)
tongcacsole(n)