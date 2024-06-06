import pandas as pd

# Membaca file Excel
df = pd.read_excel("D:\\vscode coding\\PYTHON\\database\\p.xlsx")

# Menampilkan beberapa baris pertama dari dataframe
print(df.to_string())
