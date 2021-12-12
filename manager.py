from employee import Employee


class Manager(Employee):
    def __init__(self, id,  name, address, age, number_of_employees, employee_rate):
        super().__init__(id, name, address, age)
        self.number_of_employees = number_of_employees
        self.employee_rate = employee_rate

    def calculate_salary(self):
        salary = self.number_of_employees * self.employee_rate
        return salary

    def __str__(self):
        return super().__str__() + f'The number of employees is: {self.number_of_employees} ' + \
               f'and the employee rate is: {self.employee_rate}. '
