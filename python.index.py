import mypack.my_module1  
import mypack.my_module1 as my_module


# from my_module import find_index as function1 , test,name
import datetime

import calendar

import os
courses =['history','math','physisct']

index =my_module.find_index(courses,'math')
 
print(index)
 
result = my_module.giaiphuongtring(3,4)
print(result)

# datatime
today = datetime.date.today()
print(today)

#calendar
print(calendar.isleap(2020))

#os
print(os.getcwd())

print(os.__file__)