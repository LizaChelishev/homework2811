from employee import Employee


class Worker(Employee):
    def __init__(self, id, name, address, age, hours_per_day, hour_rate):
        super().__init__(id, name, address, age)
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate

    def calculate_salary(self):
        salary = self.hours_per_day * self.hour_rate
        return salary

    def __str__(self):
        return super().__str__() + f'The number of hours per day is: {self.hours_per_day} ' + \
               f'and the hourly rate is: {self.hour_rate}. '
