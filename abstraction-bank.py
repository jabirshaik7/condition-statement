from abc import ABC, abstractmethod  

class BankAccount(ABC):  
    def __init__(self, account_holder, balance=0):  
        self.account_holder = account_holder  
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    @abstractmethod  
    def withdraw(self, amount):  
        pass  

class SavingsAccount(BankAccount):  
    def withdraw(self, amount):  
        if amount > self.balance:  
            print("Insufficient balance!")  
        else:  
            self.balance -= amount  
            print(f"{amount} withdrawn. New balance: {self.balance}")  

class CurrentAccount(BankAccount):  
    def withdraw(self, amount):  
        if amount > self.balance + 5000:  
            print("Overdraft limit exceeded!")  
        else:  
            self.balance -= amount  
            print(f"{amount} withdrawn. New balance: {self.balance}")  

savings = SavingsAccount("Alice", 10000)  
current = CurrentAccount("Bob", 2000)  

savings.deposit(2000)  # Alice deposits ₹2000  
savings.withdraw(5000)  # Alice withdraws ₹5000  
savings.withdraw(8000)  # Insufficient balance  

current.deposit(3000)  # Bob deposits ₹3000  
current.withdraw(6000)  # Allowed due to overdraft  
current.withdraw(8000)  # Overdraft limit exceeded!  

from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
    
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time, assign delivery.")

class GroceryOrder(Order):
    def process_orders(self):
        print("Processing Grocery Order: Check inventory per item, bag & dispatch.")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign secure courier.")

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Cloud Kitchen Order: Prepare dynamically, generate OTP.")

class TiffinOrder(Order):
    def process_order(self):
        print("Processing Tiffin Subscription: Schedule weekly deliveries, manage preferences.")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check pet product categories and ship.")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Seafood Order: Confirm freshness, assign chilled delivery.")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom baking, time-sensitive packaging.")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order: Bulk cooking, team coordination, special packaging.")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate prep, cold packaging.")


def handle_order(order):
    order.process_order()

orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    TiffinOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder()
]

for order in orders:
    handle_order(order)
