class Employee:

    raise_amt = 1.04
    num_of_emp =0

    def __init__(self,fisrt,last,pay):
        self.first = fisrt
        self.last = last
        self.pay = pay
        self.email = fisrt+'.'+last+'@fpt.com.vn'
        
    def fullname(self):
        return '{} {}'.format(emp_1.first,emp_1.last)


    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls,amp_str):
        fisrt,last,pay = emp_str_1.split('-')
        return cls(fisrt,last,pay)

    @classmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday()==6:
            return False
        return True

class Developer(Employee):
    pass




emp_1 = Employee('lam','nn',3000)
emp_2 = Employee('minh','pq',9090)


emp_str_1 = 'lam-nguyen-ngoc'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

dev_1 = Employee('lam','nguyen ngoc','2333')
print(dev_1.email)
# import datetime
# my_date = datetime.date(2019,5,11)

# print(Employee.is_workday(my_date))

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# Employee.set_raise_amt(1.05)
# print(emp_2.raise_amt)






# print(emp_1)
# print(emp_2)

# emp_1.first = 'lamnn'
# emp_1.last = 'ahihi'
# emp_1.email = 'lamnn@'
# emp_1.pay = 300000

# emp_2.first = 'lamnn'
# emp_2.last = 'ahihi'
# emp_2.email = 'lamnn@'
# emp_2.pay = 300000
# print(emp_1.pay)


# print(emp_2.email)
# print(emp_1.email)
# print('{} {}'.format(emp_1.first,emp_1.last))
# print(emp_1.fullname())


# Employee.fullname(emp_1)