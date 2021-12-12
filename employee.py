from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f'Worker ID: {self.id} named {self.name}. Address: {self.address} ' + \
               f'Age: {self.age} | Salary: {self.calculate_salary()}. '
