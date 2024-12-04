Звіт: Класи в Python

1. Вступ

Класи — це основний механізм об'єктно-орієнтованого програмування (ООП) у Python. Вони дозволяють об'єднувати дані та функціональність у логічні одиниці, які називаються об'єктами.

2. Основні поняття

1. Клас — це шаблон або "чертеж" для створення об'єктів.


2. Об'єкт — це екземпляр класу.


3. Методи — функції, визначені всередині класу, що виконують операції над його даними.


4. Атрибути — змінні, що зберігають дані об'єкта.



3. Створення класу

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

4. Створення об'єкта

obj = MyClass("Roman")
print(obj.greet())  # Виведе: Hello, Roman!

5. Спадкування

Класи можуть успадковувати властивості й методи інших класів.

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound())  # Виведе: Woof!

6. Інкапсуляція

Інкапсуляція дозволяє приховати внутрішню реалізацію.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Виведе: 100

7. Поліморфізм

Можливість використання одного імені методу для різних реалізацій.

class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        return "Can't fly"

penguin = Penguin()
print(penguin.fly())  # Виведе: Can't fly

8. Переваги класів у Python

Організація коду: дозволяють структурувати програми.

Повторне використання: через спадкування та композицію.

Модульність: зручне управління великими проектами.


Висновок

Класи в Python забезпечують гнучкість та ефективність розробки програмного забезпечення. Використання ООП підвищує читабельність, зручність підтримки коду та сприяє повторному використанню компонентів.


---

Якщо потрібен більш розширений звіт, повідом!

