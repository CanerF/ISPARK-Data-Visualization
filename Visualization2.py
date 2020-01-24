from main import df_Ispark, df_Ispark_saved
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
df_Ispark_Park = df_Ispark_saved[['Park Tipi','Aylık Abonelik Ücreti']]
df_Ispark_Park.columns =[column.replace(" ", "_") for column in df_Ispark_Park.columns]

Yolustu = df_Ispark_Park.query('Park_Tipi == "YOL ÜSTÜ" and Aylık_Abonelik_Ücreti != 0').mean()
Acik = df_Ispark_Park.query('Park_Tipi == "AÇIK OTOPARK" and Aylık_Abonelik_Ücreti != 0').mean()
Kapali = df_Ispark_Park.query('Park_Tipi == "KAPALI OTOPARK" and Aylık_Abonelik_Ücreti != 0').mean()
list_park_ücreti = [Yolustu.round(2),Kapali.round(2), Acik.round(2)]
list_park_tipi = ['Yol Üstü', 'Kapalı Otopark', 'Açık Otopark']

plt.figure(figsize=(15,10))
sns.barplot(x = list_park_tipi, y = list_park_ücreti, palette= "muted")
plt.xticks(rotation = 45)
plt.xlabel('Park Tipi')
plt.ylabel("Ortalama Ücret(TL)")
plt.title('PARK TİPLERİNE GÖRE AYLIK ORTALAMA ABONELİK ÜCRETİ GRAFİĞİ')
plt.grid(axis = 'y', linestyle = '-')
plt.show()








