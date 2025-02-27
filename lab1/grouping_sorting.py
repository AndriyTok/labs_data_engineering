import pandas as pd
df = pd.read_csv("train_1.csv")

# 📌 1. Відсортувати по зростанню (ascending) і спаданню (descending)
df_sorted_asc = df.sort_values(by="Sales", ascending=True)  # По зростанню
df_sorted_desc = df.sort_values(by="Sales", ascending=False)  # По спаданню

print("🔹 Відсортовано по зростанню:\n", df_sorted_asc.head())
print("🔹 Відсортовано по спаданню:\n", df_sorted_desc.head())

# 📌 2. Групування по одній колонці (знаходження max Sales по кожному магазину)
grouped_one = df.groupby("Store")["Sales"].max()
print("🔹 Максимальні продажі по магазинах:\n", grouped_one.head())

# 📌 3. Групування по двох колонках (максимальні продажі по кожному магазину за кожен день тижня)
grouped_two = df.groupby(["Store", "DayOfWeek"])["Sales"].max()
print("🔹 Максимальні продажі по магазинах і днях тижня:\n", grouped_two.head())

# 📌 4. Групування по трьох колонках (максимальні продажі з урахуванням відкриття магазину)
grouped_three = df.groupby(["Store", "DayOfWeek", "Open"])["Sales"].max()
print("🔹 Максимальні продажі з урахуванням відкриття магазину:\n", grouped_three.head())

# 📌 5. Агрегація даних (agg) - середні та максимальні продажі по магазинах
agg_sales = df.groupby("Store").agg({"Sales": ["mean", "max"], "Customers": "sum"})
print("🔹 Агрегація даних (середні та макс. продажі, сума покупців):\n", agg_sales.head())

# 📌 6. Фільтрація по значенню (наприклад, вибрати всі магазини, де продажі більше 5000)
filtered_sales = df[df["Sales"] > 5000]
print("🔹 Магазини з продажами більше 5000:\n", filtered_sales.head())

# 📌 7. Отримати рядки з певним значенням параметру (наприклад, всі магазини, які закриті)
closed_stores = df[df["Open"] == 0]
print("🔹 Магазини, які закриті:\n", closed_stores.head())

# 📌 8. Написати довільний запит (query)
query_result = df.query("Sales > 5000 and Customers > 1000")  # Магазини, де продажі >5000 і покупців >1000
print("🔹 Магазини з продажами >5000 і покупцями >1000:\n", query_result.head())
