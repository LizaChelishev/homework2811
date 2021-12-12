from employee import Employee


class Contractor(Employee):
    def __init__(self, id, name, address, age, number_of_projects, project_rate):
        super().__init__(id, name, address, age)
        self.number_of_projects = number_of_projects
        self.project_rate = project_rate

    def calculate_salary(self):
        salary = self.number_of_projects * self.project_rate
        return salary

    def __str__(self):
        return super().__str__() + f'The number of projects is: {self.number_of_projects} ' + \
               f'and the project rate is: {self.project_rate}. '
