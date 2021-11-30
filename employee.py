from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    @abstractmethod
    def calculate_salary(self, hours_per_day, hour_rate):
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate
        salary = hours_per_day * hour_rate
        return salary

    @abstractmethod
    def __str__(self):
        print(f'Worker number: {self.id} named {self.name}. Address: {self.address} +\
        | Age: {self.age} | Salary: {self.calculate_salary()}')




