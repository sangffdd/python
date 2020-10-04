s=m/(h*h)
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