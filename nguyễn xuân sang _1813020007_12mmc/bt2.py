print("đề 2")
print("bài 2 nhập tháng xuất ra mùa ")
def mua(s):
    if ( s == 1 or s <= 3):
        return("mùa Xuân")
    elif (s == 4 or s <= 6):
        return("mùa Hạ")
    elif ( s == 7 or s <= 9):
        return("Thu")
    elif ( s == 10 or s <=12):
        return("mùa Đông")
    else:
        return("nhập sai tháng")
if __name__ == "__main__":
    s=int(input("nhập vào 1 tháng trong năm :"))
    print("mùa tương ứng với tháng đó là :")
    print(mua(s))