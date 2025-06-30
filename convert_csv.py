import pandas as pd

# Загружаем оригинальный файл с brand и domain
df = pd.read_csv("data/original_phishing.csv")

# Удаляем дубликаты и пустые строки
df = df.dropna()
df = df.drop_duplicates()

# Добавляем метку Phishing
df["label"] = "Phishing"

# Оставляем только нужные колонки
df = df[["domain", "label"]]

# Сохраняем
df.to_csv("data/phishing_data.csv", index=False)
print("✅ Файл data/phishing_data.csv создан!")