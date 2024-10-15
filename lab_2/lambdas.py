#Лямбда-функції в Python — це анонімні функції, які можна визначити за допомогою ключового слова `lambda`. Вони часто використовуються для простих операцій, особливо коли потрібно передати функцію як аргумент у інші функції, такі як `map()`, `filter()`, або `sorted()`.

### Основна структура лямбда-функції

#ямбда-функція має наступний синтаксис:

lambda аргументи: вираз

### Переваги лямбда-функцій
#1. **Анонімність**: Лямбда-функції не потребують імені, що робить їх корисними для коротких функцій.
#2. **Консьюмеризм**: Можна використовувати їх в місцях, де звичайна функція не підходить, наприклад, у функціях вищого порядку.

### Приклад

#Ось приклад використання лямбда-функцій для обробки списку чисел:

# Список чисел
numbers = [1, 2, 3, 4, 5]

# Використання лямбда-функції з map для піднесення до квадрату
squared = list(map(lambda x: x ** 2, numbers))

# Використання лямбда-функції з filter для фільтрації парних чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Використання лямбда-функції з sorted для сортування за зворотним порядком
sorted_numbers = sorted(numbers, key=lambda x: -x)

# Вивід результатів
print("Піднесені до квадрату:", squared)
print("Парні числа:", even_numbers)
print("Сортовані числа (зворотний порядок):", sorted_numbers)

### Пояснення:

#1. **`map()`**: Використовується для застосування лямбда-функції до кожного елемента списку `numbers`. У цьому випадку кожен елемент підноситься до квадрату.

#2. **`filter()`**: Фільтрує список, залишаючи тільки парні числа. Лямбда-функція повертає `True` для парних чисел і `False` для непарних.

#3. **`sorted()`**: Сортує список `numbers` у зворотному порядку. Лямбда-функція вказує, що елементи мають бути відсортовані за їх від’ємними значеннями.

### Результат:

#Код виведе:

#Піднесені до квадрату: [1, 4, 9, 16, 25]
#Парні числа: [2, 4]
#Сортовані числа (зворотний порядок): [5, 4, 3, 2, 1]

### Висновок

#Лямбда-функції в Python є зручним інструментом для створення коротких функцій, особливо коли вони потрібні на раз. Вони часто використовуються для обробки колекцій даних і можуть зробити код компактнішим та легшим для читання. Проте для складніших функцій краще використовувати звичайні функції, щоб уникнути зменшення читабельності коду.