from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, name, purchase_amount):
        self.name = name
        self.purchase_amount = purchase_amount

    @abstractmethod
    def calculate_final_amount(self):
        pass

class RegularCustomer(Customer):
    def calculate_final_amount(self):
        return self.purchase_amount

class VIPCustomer(Customer):
    def calculate_final_amount(self):
        return self.purchase_amount * 0.80

class WholesaleCustomer(Customer):
    def calculate_final_amount(self):
        return self.purchase_amount * 0.60


def print_invoice(customer_obj):
    final_price = customer_obj.calculate_final_amount()
    print(f"Customer: {customer_obj.name} | The Final Price: {final_price}")


customers = [
    RegularCustomer("Ahmed", 1000),
    VIPCustomer("Ali", 1000),
    WholesaleCustomer("Company", 1000)
]

for cust in customers:
    print_invoice(cust)