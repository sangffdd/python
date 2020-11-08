print ("bài tập 10.1")
f = open("abc.txt",'w',encoding='Utf8')

f.write("hello world")
f.close()

print ("bài tập 10.2 ")
f = open("abc.txt",'r',encoding='Utf8')
str = f.read(5)
print ('Noi dung file cua ban la:\n', str)

print ("bài tập 10.3")


print ("bài tập 10.4")
f = open("abc.txt",'a',encoding='utf8')
f.write("sang pro")
f.close

print ("Bài 10.5 Viết chương trình xóa một tập tin đang có trên hệ thống.)
import os
chuoi=str(input("nhap chuoi: "))
if os.path.exists(chuoi):
    print("đã xóa tap tin ",chuoi)
    os.remove(chuoi)
else:
    print("khong tim thay tap tin  ",chuoi)
