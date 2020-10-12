print('Bài tập 01: Viết chương trình nhập xuất mảng 1 chiều (List )')
print('a. Tính tổng của mảng 1 chiều')
u = int(input("nhập vào giá trị u= "))
def tong(u):
    arr = [] 
    tong = 0 
    for s in range (u):
        o = input(f"nhập vào 1 giá trị[{s}]: ")
        arr.append(int(o))
        tong+=arr[s]
    return tong
print("tổng của các phần tử trong mảng 1 chiều là : ",tong(u))
print('b. Tính tích của mảng 1 chiều')
def tich(u):
    arr = [] 
    tich = 1
    for k in range (u):
        t = input(f"nhập vào giá trị[{k}]: ")
        arr.append(int(t))
        tich*=arr[k]
    return tich
print("Tích của các phần tử trong mảng 1 chiều : ",tich(u))
print(" c. Tìm giá trị lớn nhất")
def max(u):
    arr = []
    
    for i in range (u):
        s = input(f"nhập vào giá trị của mảng [{i}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > m):
            m=arr[i]
    return m
print("số lớn nhất tìm được trong mảng là: ",max(u))
print(" c. Tìm giá trị nhỏ nhất")
def min(u):
    arr = []
    
    for t in range (u):
        s = input(f"nhập vào giá trị của mảng [{t}]: ")
        arr.append(int(s))
    m = arr[0]
    for i in range (1, len(arr)):
        if(arr[t] < m):
            m=arr[t]
    return m
print("số nhỏ nhất tìm được trong mảng là: ",min(u))
print("e.tìm các số lẻ trong mảng")
def sole(u):
    result = []
    arr = []
    
    for s in range (u):
        o = input(f"nhập vào giá trị của mảng[{s}]: ")
        arr.append(int(o))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 != 0 ):
            result.append(arr[s])
    return result
print("các số lẻ cần tìm trong mảng là : ",sole(u))
print('f.tìm số chẵn trong mảng')
def sochan(u):
    result = []
    arr = []
    
    for s in range (u):
        y = input(f"nhập vào giá trị cần tìm trong mảng[{s}]: ")
        arr.append(int(y))
    for s in range(0,len(arr)):
        if ( arr[s] % 2 == 0 ):
            result.append(arr[s])
    return result
print("các số chẵn cần tìm trong một mảng là: ",sochan(u))
print("bài 3 trên zalo")
list1=[4,5,6]
arr= []
u = int(input("nhập vào giá trị u= "))
for s in range (u):
    i = input(f"nhập vào 1 giá trị[{s}]: ")
    arr.append(int(i))
print(arr)
print(list1)
print(list1 + arr)
print("bài 2 trong pdf")
u =int(input("input u value= "))
def timidbaihat(u):
    result =[]
    arr = []
    count =0
    
    for s in range (u):
        i = input(f"input random value[{s}]: ")
        arr.append(int(i))
    for s in arr:
        if s not in result:
            result.append(s)
            count+=1
    return count,result
print(timidbaihat(u))

