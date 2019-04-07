# list trong python là cấu trúc  mãng các phần tử có index có thứ tự
# muốn tạo phẩn tử cá key và value thì sử dụng cấu trức Dictionaru
# list được khai báo như mảng trong JSON

number = [1,2,3,4,5]
render = ['vatlydaicuong','hoadaicuong','thuchanhlydaicuong']

# truy xuát từng phnầ tử bằng index
print(number[2])
print(render[-2])

# so luong phan tu
# if index < len(number):
#     number[index]
# Exception :


#nối hai mang
a =[1,2]
b = [3,4]
print('noi hai list',a+b) #noi hai mang [1, 2, 3, 4]


# them phan tu vao mang dung list.append(newvalue) đuôc them vào cuối mãng

k= [1,2,3,4,5]
print(k)
k.append(9)
print(k)


#lay phần tử cuối mãng
mynumber = k.pop()
print(mynumber)

# tìm giá trị trong mang dùng list.index(obj)
alist = [123,'xyz','abc']
print(alist.index(123))


#reverse 
number.reverse()
print(number)


# sắp xếp giá trị các phần tử
p =[7,4,8,9,1]
print(p)
p.sort()
print(p)
