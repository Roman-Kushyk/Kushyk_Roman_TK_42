#Ось детальніший приклад контекст-менеджера в Python, який управляє ресурсами, такими як відкриття і закриття файлів. У цьому прикладі ми створимо свій контекст-менеджер для роботи з текстовим файлом:

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Відкриваємо файл у вказаному режимі
        self.file = open(self.filename, self.mode)
        return self.file  # Повертаємо об'єкт файлу для використання

    def __exit__(self, exc_type, exc_value, traceback):
        # Закриваємо файл, якщо він відкритий
        if self.file:
            self.file.close()
        # Можемо обробити виключення тут, якщо потрібно
        if exc_type:
            print(f"Виникла помилка: {exc_value}")

# Використання контекст-менеджера
filename = 'example.txt'

with FileManager(filename, 'w') as file:
    file.write("Привіт, світ!\n")
    file.write("Це приклад контекст-менеджера.\n")

# Перевірка, чи запис було успішно здійснено
with FileManager(filename, 'r') as file:
    content = file.read()
    print("Зміст файлу:")
    print(content)

### Пояснення:

#1. **Клас `FileManager`**: Це наш контекст-менеджер, який приймає ім'я файлу та режим (наприклад, `'w'` для запису або `'r'` для читання).
   
#2. **Метод `__enter__`**: Відкриває файл у вказаному режимі і повертає об'єкт файлу для подальшого використання.

#3. **Метод `__exit__`**: Закриває файл, якщо він був відкритий. Якщо сталася помилка (виключення), вона буде виведена на екран.

#4. **Використання контекст-менеджера**: У блоці `with` ми можемо записати дані у файл, а потім знову використати той же контекст-менеджер для читання з файлу.

### Результат:

#При виконанні цього коду у файлі `example.txt` буде записано:


#Привіт, світ!
#Це приклад контекст-менеджера.

#І на екрані буде виведено:
#Зміст файлу:
#Привіт, світ!
#Це приклад контекст-менеджера.
