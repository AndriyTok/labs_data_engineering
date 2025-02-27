# Підключити бібліотеку pandas для зчитування даних за допомогою python

import pandas as pd

# Зчитати дані у DataFrame за допомогою методу read_...

df = pd.read_csv("train_1.csv")

# Використати методи pandas для роботи з DataFrame:
# Вивести head() tail() sample() .shape, .columns, .index .dtypes. info

print("🔹 Перші 5 рядків:\n", df.head())  # Показує перші 5 рядків
print("🔹 Останні 5 рядків:\n", df.tail())  # Показує останні 5 рядків
print("🔹 Випадковий рядок:\n", df.sample())  # Випадковий рядок
print("🔹 Розмірність таблиці (рядки, колонки):", df.shape)  # Кількість рядків і колонок
print("🔹 Назви колонок:", df.columns)  # Всі колонки
print("🔹 Індекси рядків:", df.index)  # Діапазон індексів
print("🔹 Типи даних у колонках:\n", df.dtypes)  # Типи даних
print("🔹 Загальна інформація про DataFrame:")
df.info()  # Основна інформація

#  Створити нову колонку. В колонку записати суму значень двох колонок з таблиці.

df["Revenue"] = df["Sales"] * df["Customers"]
print("🔹 Оновлена таблиця з колонкою Revenue:\n", df.head())





