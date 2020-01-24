import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

path = "C:/Users/Caner Filiz/Desktop/Python/ispark-otoparklarna-ait-bilgiler.xlsx"
sheetName ="İSPARK Otoparklarına Ait B."
df_Ispark_saved = pd.read_excel(path, sheetName)
pd.set_option('display.max_columns', None)
df_Ispark_Ilce = df_Ispark_saved[['Park ID', 'İlçe']]
df_Ispark_Ilce.columns =[column.replace(" ", "_") for column in df_Ispark_Ilce.columns]

def get_Ilce():
    Ilce_listesi = []
    for i in df_Ispark_saved['İlçe']:
        if i in Ilce_listesi:
            continue
        else:
            Ilce_listesi.append(i)
    return Ilce_listesi
Ilce_listesi = get_Ilce()
Id_toplami = []
Id_toplami2 = []
for i in Ilce_listesi:
    df = df_Ispark_Ilce['İlçe'] == i
    df1 = df_Ispark_Ilce[df]
    counter = df1['Park_ID'].shape[0]
    Id_toplami.append(counter)

fig = go.Figure(data = [go.Scatter(
    x = Ilce_listesi,
    y = Id_toplami, mode = 'markers',
    marker_size = Id_toplami,
    marker = dict(
            color=['rgb(200, 0, 230)']*33,
            opacity=[0.7]*33
    )
)])
fig.update_layout(
    title='İLÇELERE GÖRE PARK YERİ SAYISI GRAFİĞİ',
    xaxis=dict(
        title='İlçeler',
        gridcolor='white',
        gridwidth=1,
    ),
    yaxis=dict(
        title='Park Yeri Sayısı',
        gridcolor='white',
        gridwidth=1,
    )
)
fig.show()




