A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except Exception as e:
    print(f"Виникла помилка: {e}")
finally:
    print("Код в блоці finally виконується завжди.")
