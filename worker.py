from abc import ABC

from employee import Employee

class Worker(Employee, ABC):
def __init__(self, name, address, age, hours_per_day, hour_rate):
    super(self.__class__, self).__init__(self, name, address, age)

def calculate_salary(self):
    super(self.__class__, self)

def __str__(self):
    return super.__str__()



