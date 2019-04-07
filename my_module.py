print('import my_module...')
test = 'test string' # this is string


def name():
    print('hello my name in lamnn')

def giaiphuongtring(a,b):
    if(a==0 | b==0):
        return('nhap sai roi')
    elif(a==0):
        return('phuong trinh vo nghiem')
    elif(b==0):
        return('phuong trinh co vo so nghiem')
    else:
        return('ket qua',-b/a)
    
def Strace_elment():
    letter = 'well come SCC'
    for element in letter:
        print(element)


def find_index(to_serch,target):
    for i,value in enumerate(to_serch):
        if value == target:
            return 1
    return -1

