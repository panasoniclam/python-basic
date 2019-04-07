#dictionary là cấu trức mãng, các phần từ bao gồm key vá value
#tuong tự như một object JSON
# dictionary được khai báo trong dấu {} dưới dạng {key:value}

mydistionary = {'1':1,'a':4,3:6,2.3:9}
print(mydistionary[2.3])

#thêm một phần tử vào dictionary object
mydistionary['key'] = 'value'
print(mydistionary) #{'1': 1, 'a': 4, 3: 6, 2.3: 9, 'key': 'value'}


# xóa toàn bộ phẩn tử bên trong một object dictionary
cleardistionary ={'key':'value',2:'X'}
print(cleardistionary)#{'key': 'value', 2: 'X'}
cleardistionary.clear()
print(cleardistionary)#{}

# kiểm tra một key có tồn tại ko
dictionary_test = {'key':'value',1:'A',2:'B'}
 