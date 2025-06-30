import pandas as pd

df = pd.read_csv("data/original_phishing.csv")

df = df.dropna()
df = df.drop_duplicates()

df["label"] = "Phishing"

df = df[["domain", "label"]]

df.to_csv("data/phishing_data.csv", index=False)
print("Файл data/phishing_data.csv создан!")
