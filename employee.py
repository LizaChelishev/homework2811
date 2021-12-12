from abc import ABC, abstractmethod
from datetime import date


class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, year_of_birth):
        self.id = id
        self.name = name
        self.address = address
        self.year_of_birth = year_of_birth

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f'Worker ID: {self.id} named {self.name}. Address: {self.address} ' + \
               f'Age: {self.get_age()} | Salary: {self.calculate_salary()}. '

    def get_age(self):
        todays_date = date.today()
        age = todays_date.year - self.year_of_birth
        return age
