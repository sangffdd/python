print("đề 2")
print("bài 3 : Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13),nếu chạy đến số 13 thì không chạy nữa")
def tinh_tong(u):
    tong = 0
    for s in range (1,u+1):
        if (s == 13 ):
            break
        else:
            tong += s
        
    return tong
if __name__ == "__main__":
    u=int(input("nhập một giá trị từ bàn phím:"))
    print("tổng các giá tri từ 1 đến ",u," là: ",tinh_tong(u))