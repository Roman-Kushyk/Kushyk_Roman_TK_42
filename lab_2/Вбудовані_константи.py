#Вбудовані константи
#В Python є кілька вбудованих констант, які можуть використовуватися в програмуванні. Ось детальні приклади:

### 1. `True` та `False`
#Ці константи використовуються для представлення логічних значень.


is_active = True
is_deleted = False

if is_active:
    print("Об'єкт активний.")
else:
    print("Об'єкт неактивний.")

### 2. `None`
#Константа `None` використовується для позначення відсутності значення або об'єкта.

result = None

def calculate(value):
    if value < 0:
        return None
    return value * 2

result = calculate(-1)

if result is None:
    print("Результат не визначено.")
else:
    print(f"Результат: {result}")

### 3. `float('inf')` та `float('-inf')`
#Ці константи представляють позитивну та негативну нескінченність.

positive_infinity = float('inf')
negative_infinity = float('-inf')

print(positive_infinity > 1000000)  # True
print(negative_infinity < -1000000)  # True

### 4. `math.pi` та `math.e`
#Ці константи з модуля `math` представляють числа π та e.

import math

circle_area = math.pi * (5 ** 2)  # Площа кола з радіусом 5
print(f"Площа кола: {circle_area}")

exponential_value = math.e ** 2  # Значення e в квадраті
print(f"e^2: {exponential_value}")


### 5. `string.ascii_letters`, `string.ascii_lowercase`, `string.ascii_uppercase`
#Ці константи з модуля `string` представляють набори символів.


import string

print(string.ascii_letters)  # Всі літери латинського алфавіту
print(string.ascii_lowercase)  # Маленькі літери
print(string.ascii_uppercase)  # Великі літери

#Ці приклади демонструють, як можна використовувати вбудовані константи в Python для різних цілей.

# Виведення констант
print("Перша константа:", True)
print(f"Друга константа: {None}")
print("Третя константа:", False)
