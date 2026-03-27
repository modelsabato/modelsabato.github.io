import pandas as pd

df = pd.read_csv('datos_pd.csv')
print(df)
for col in df:
    df[col] = df[col].sort_values(ignore_index=True)
print(df)

with open('datos.csv', 'rt') as f:
    lines = f.readlines()
