print("đề 2")
print("Bài 4: Giả sử có một chuỗi như sau: “0983876207;0918295063;0002;05:18:25;”, tách chuỗi trên thành từng phần riêng biệt")
def tinhtiencuocgoi(chuoi):
    
    chuoi1 = chuoi.split(";")
    thoi_gian = chuoi1[3].split(":")
    tong_so_phut = float(thoi_gian[0]) * 60 + float(thoi_gian[1]) + float(thoi_gian[2]) / 60
    money = tong_so_phut * 2500
    return int(money)
if __name__ == "__main__":
    chuoi=str(input("nhập vào chuỗi đã cho trên đề: "))
    print(" giá cước trên là: ",tinhtiencuocgoi(chuoi))
    
