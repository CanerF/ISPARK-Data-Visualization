from main import df_Ispark
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
df_Ispark_Park = df_Ispark[['Park Tipi','Aylık Abonelik Ücreti']]
df_Ispark_Park.columns =[column.replace(" ", "_") for column in df_Ispark_Park.columns]

Yolustu = df_Ispark_Park.query('Park_Tipi == "YOL ÜSTÜ" and Aylık_Abonelik_Ücreti != 0').mean()
Acik = df_Ispark_Park.query('Park_Tipi == "AÇIK OTOPARK" and Aylık_Abonelik_Ücreti != 0').mean()
Kapali = df_Ispark_Park.query('Park_Tipi == "KAPALI OTOPARK" and Aylık_Abonelik_Ücreti != 0').mean()
list_park_ücreti = [Yolustu.round(2),Acik.round(2),Kapali.round(2)]
list_park_tipi = ['Yol Üstü', 'Açık Otopark', 'Kapalı Otopark']

plt.figure(figsize=(15,10))
sns.barplot(x = list_park_tipi, y = list_park_ücreti, color='blue', alpha = 0.4)
plt.xticks(rotation = 45)
plt.xlabel('Park Tipi')
plt.ylabel("Ortalama Ücret")
plt.title('PARK TİPLERİNE GÖRE AYLIK ORTALAMA ABONELİK ÜCRETİ GRAFİĞİ')
plt.grid(axis = 'y', linestyle = '-')
plt.show()








