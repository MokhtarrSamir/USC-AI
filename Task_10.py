from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass
    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(Employee):
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    def calculate_bonus(self):
        return self.salary * 0.10

mng = Manager(1000)
dev = Developer(1000)

print(mng.salary, mng.calculate_bonus())
print(mng.salary, dev.calculate_bonus())