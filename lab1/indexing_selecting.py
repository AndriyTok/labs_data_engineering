import pandas as pd
df = pd.read_csv("train_1.csv")

# 📌 1. Вибрати декілька колонок і рядків
selected_columns = df[["Store", "Date", "Sales"]].head(10)  # Перші 10 рядків із колонками Store, Date, Sales
print("🔹 Вибрані колонки та рядки:\n", selected_columns)

# 📌 2. Вибрати декілька колонок і рядків за допомогою .loc (по імені)
selected_loc = df.loc[0:5, ["Store", "Sales", "Customers"]]  # Перші 6 рядків (від 0 до 5) за назвами колонок
print("🔹 Вибірка за .loc:\n", selected_loc)

# 📌 3. Вибрати декілька колонок і рядків за допомогою .iloc (по індексу)
selected_iloc = df.iloc[0:5, [0, 3, 4]]  # Перші 5 рядків (від 0 до 4) і колонки 0, 3, 4
print("🔹 Вибірка за .iloc:\n", selected_iloc)

# 📌 4. Видалити непотрібні колонки (метод drop)
df_dropped = df.drop(columns=["StateHoliday"])  # Видаляємо колонку StateHoliday
print("🔹 Таблиця після видалення колонки:\n", df_dropped.head())

# 📌 5. Видалити непотрібні рядки (наприклад, перші 2)
df_dropped_rows = df.drop(index=[0, 1])
print("🔹 Таблиця після видалення рядків 0 та 1:\n", df_dropped_rows.head())

# 📌 6. Використання conditional selection (вибірка рядків за умовою)
filtered_df = df[df["Sales"] > 5000]  # Вибираємо рядки, де Sales > 5000
print("🔹 Рядки з продажами більше 5000:\n", filtered_df.head())

# 📌 7. Використання set_index() (зміна індексу)
df_indexed = df.set_index("Date")  # Робимо колонку Date індексом
print("🔹 Таблиця з новим індексом (Date):\n", df_indexed.head())