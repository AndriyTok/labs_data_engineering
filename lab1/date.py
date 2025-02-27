import pandas as pd
from datetime import datetime

df = pd.read_csv("train_1.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")  # Конвертація у формат дати
today = datetime.today()

# 📌 Рахуємо кількість місяців до сьогодні
df["Months_To_Today"] = df["Date"].apply(lambda x: (today.year - x.year) * 12 + (today.month - x.month))

# 📌 Виводимо результат
print("🔹 Перетворення дати у кількість місяців до сьогодні:\n", df[["Date", "Months_To_Today"]].head())
