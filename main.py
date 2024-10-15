import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_2020 = pd.read_csv('acidentes2023.csv', sep=';', encoding="Windows-1252")

df_2020['data_inversa'] = pd.to_datetime(df_2020['data_inversa'], format='%Y-%m-%d')

df_agrupado = df_2020.groupby('data_inversa')['mortos'].sum().reset_index()

df_agrupado['mes'] = df_agrupado['data_inversa'].dt.month

df_filtrado = df_agrupado[(df_agrupado["mes"] == 11) | (df_agrupado["mes"] == 12)]

print(df_filtrado)

plt.figure(figsize=(12, 6))
plt.plot(df_filtrado['data_inversa'], df_filtrado['mortos'], marker='o')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Número de Vítimas')
plt.title('Evolução do Número de Vítimas (Nov-Dez 2023)')
plt.grid(True)
plt.show()