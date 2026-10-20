class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age)
        self.salary = salary
        self.job = job

    def raise_salary(self, per):
        per /= 100
        self.salary += self.salary * per

emp = Employee("Ahmed", 30, 5000, "Engineer")

emp.raise_salary(10)

print(emp.salary)