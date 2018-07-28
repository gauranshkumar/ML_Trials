class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = self.first + '.'+ self.last + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return self.first + ' ' + self.last


emp_1 = Employee('Raj','Kumar',50000)
#emp_2 = Employee()

print('{}'.format(emp_1.full_name()))