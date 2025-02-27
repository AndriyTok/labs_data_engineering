import pandas as pd

# Створимо тестовий DataFrame
data = {"Store": [1, 2, 3, 4, 5],
        "Sales": [5000, 3000, 7000, 2000, 6000],
        "Customers": [300, 150, 400, 100, 350]}
df = pd.DataFrame(data)

# 📌 Сортування за "Sales" (за замовчуванням - ascending=True)
sorted_df_asc = df.sort_values(by="Sales")

# 📌 Сортування за "Sales" в спадаючому порядку (ascending=False)
sorted_df_desc = df.sort_values(by="Sales", ascending=False)

print("🔹 Сортування за зростанням:\n", sorted_df_asc)
print("\n🔹 Сортування за спаданням:\n", sorted_df_desc)

import numpy as np

# Додаємо відсутні значення (NaN)
df.loc[2, "Sales"] = np.nan

# 📌 Видалення рядків із NaN (за замовчуванням how='any')
drop_any = df.dropna()

# 📌 Видалення лише рядків, де всі значення NaN (how='all')
drop_all = df.dropna(how='all')

# 📌 Видалення колонок із NaN (axis=1)
drop_columns = df.dropna(axis=1)

print("🔹 Видалено рядки з будь-якими NaN:\n", drop_any)
print("\n🔹 Видалено лише рядки, де ВСІ значення NaN:\n", drop_all)
print("\n🔹 Видалено колонки, які містять NaN:\n", drop_columns)
