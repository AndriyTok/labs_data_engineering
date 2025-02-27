import pandas as pd
df = pd.read_csv("train_1.csv")

# 📌 1. Метод value_counts() - підрахунок унікальних значень у колонці
store_counts = df["Store"].value_counts()  # Підрахунок кількості кожного магазину
print("🔹 Кількість записів для кожного магазину:\n", store_counts.head())

# 📌 2. Метод unique() - отримати унікальні значення
unique_days = df["DayOfWeek"].unique()  # Унікальні дні тижня
print("🔹 Унікальні дні тижня:\n", unique_days)

# 📌 3. Метод sum() - загальна сума по колонці
total_sales = df["Sales"].sum()  # Сума всіх продажів
print("🔹 Загальні продажі:", total_sales)

# 📌 4. Метод mean() - середнє значення по колонці
average_customers = df["Customers"].mean()  # Середня кількість покупців
print("🔹 Середня кількість покупців:", average_customers)

# 📌 5. Метод map() - змінюємо значення у колонці
# Припустимо, що колонка "Open" має значення 1 та 0, замінимо їх на "Відкрито" та "Закрито"
df["Open_Status"] = df["Open"].map({1: "Відкрито", 0: "Закрито"})
print("🔹 Перетворення значень у колонці Open:\n", df[["Open", "Open_Status"]].head())

# 📌 6. Метод map() з lambda виразом - зміна значень через функцію
# Переведемо "Customers" у категорію: більше 1000 - "БагатоCustomers", менше - "Мало"
df["Customer_Category"] = df["Customers"].map(lambda x: "Багато" if x > 1000 else "Мало")
print("🔹 Категоризація покупців:\n", df[["Customers", "Customer_Category"]].head())