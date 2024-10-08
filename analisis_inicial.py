import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3  as sql
def espacios ():
    print("\n"*2)

# direccion_nuevo="data_01_nuevo.csv"
# data_01 = pd.read_csv(direccion_nuevo)
sql_connection = sql.connect('data_01_nuevo.db')
data_01 = pd.read_sql_query("SELECT * FROM data_01_nuevo", sql_connection)
# print(data_01.head())
data_01['date'] = pd.to_datetime(data_01['date'])
data_01.set_index('date', inplace=True)

# print(data_01.head())
# espacios()
print(data_01.info())
espacios()
print(data_01.describe())
espacios()
plt.figure(figsize=(12, 6))
sns.heatmap(data_01.corr(), annot=True, cmap='coolwarm')
plt.title('Correlación de variables')
# plt.show()
data_01["Fe rise"] = data_01["% Iron Concentrate"] - data_01["% Iron Feed"]
columnas=data_01.columns
print(columnas)
columnas_2=data_01.columns[-2:]

# for col in columnas:
#     for i in columnas_2:
#         plt.figure(figsize=(12, 6))
#         sns.scatterplot(data=data_01_nuevo, x=data_01_nuevo[i], y=col)
#         plt.title(f'{col} vs {i}')
#         plt.savefig(fname=f'{col}_vs_{i}.png')
#         plt.close()
# plt.figure(figsize=(12, 6))
# sns.lineplot(data=data_01_nuevo, x=data_01_nuevo.index, y=data_01_nuevo.columns[0])
# plt.show()