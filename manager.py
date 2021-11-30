from abc import ABC

from employee import Employee

class Manager(Employee):
    def __init__(self, name, address, age ,number_of_employers, employee_rate):
        super(Manager, self).__init__(self, name, address, age)
        self.number_of_employers = number_of_employers
        self.employee_rate = employee_rate

    def calculate_salary(self, number_of_employers, employee_rate):
        salary_manager = number_of_employers * employee_rate
        return salary_manager

    def __str__(self):
        return super.__str__()