# 1. Move All Zeros to End
arr = [0, 1, 0, 3, 12]
result = [x for x in arr if x != 0] + [0] * arr.count(0)
print(result)   # [1, 3, 12, 0, 0]

# 2. Armstrong Number
num = 153
s = sum(int(d)**len(str(num)) for d in str(num))
print("Armstrong" if s == num else "Not Armstrong")

# 3. Rotate List Right by K
arr = [1, 2, 3, 4, 5]; k = 2
k %= len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)  # [4, 5, 1, 2, 3]

# 4. Pattern Compression
s = "aaabbcddd"; out = ""
i = 0
while i < len(s):
    count = 1
    while i+1 < len(s) and s[i] == s[i+1]:
        count += 1; i += 1
    out += s[i] + str(count); i += 1
print(out)   # a3b2c1d3

# 1. Electricity Bill Calculator
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10
print("Total Bill =", bill)

# 2. Pattern Printing
n = 1
for i in range(1, 5):
    for j in range(i):
        print(n, end=" "); n += 1
    print()

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name; self.balance = balance
    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance: self.balance -= amount
        else: print("Insufficient balance")
    def display_balance(self): print(f"{self.name}'s Balance: {self.balance}")

acc = BankAccount("Jabir", 1000)
acc.deposit(500); acc.withdraw(300); acc.display_balance()

# 4. File Handling – Student Data
with open("students.txt", "w") as f:
    for i in range(3):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        f.write(name + " " + marks + "\n")

with open("students.txt", "r") as f:
    data = f.read()
print("Student Data:\n", data)

# 5. Inheritance Program
class Person:
    def __init__(self, name, age):
        self.name = name; self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age); self.salary = salary
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

emp = Employee("Jabir", 25, 50000)
emp.display()

