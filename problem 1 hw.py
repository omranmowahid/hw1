"""Ahmad Emran - roll no (4) - IT"""


# 1. Create a class called Person with attributes name and age. Create an object of the class and print its attributes.
# class Person:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
# perosn = Person(20, 'ahmad')
# print(perosn.age)
# 14. Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check the balance.

# class BankAccount:
#     def __init__(self, init_account_number, init_balance = 0):
#         self.__account_number = init_account_number
#         self.__balance = init_balance
#
#     def deposit(self, amount):
#         if amount < 0:
#             print('should not negative')
#         else:
#             self.__balance += amount
#
#     def with_draw(self, amount):
#         if amount < 0:
#             print('should not negative')
#         else:
#             self.__balance -= amount
#
#     def detail(self):
#         print(self.__balance)
#
# bank = BankAccount(123, 100)
# bank.detail()


# 19. Create a class Company with attributes name and emploees (a list of Employee objects). Provide methods to add and remove employees. '

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Company:
    def __init__(self, name):
        self.name = name
        self.employee = []

    def add_employee(self, person):
        self.employee.append(person)

    def revome_employee(self, person):
        self.employee.remove(person)

    def detail(self):
        return self.employee

person1 = Person('ahmad')

company = Company('facebook')
company.add_employee(perosn1)




























