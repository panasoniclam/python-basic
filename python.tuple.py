#là mảng tương từ như list, nhưng tuple khác list ở chỗ các phần tử của tuple
# chứa trong dấu ()
# một tuple khi khai báo thì không thay đồi đc giá trị
# không hổ trợ append() và pop()
mytuple = (1,2,3,4)
print(mytuple)
# truy xuất theo index,range thì giống list
print(mytuple.index(2))
#noi hai tuple
a = (1,2,3)
b= (4,5,6)
print('nối hai tuple',a+b) #(1, 2, 3, 4, 5, 6)
