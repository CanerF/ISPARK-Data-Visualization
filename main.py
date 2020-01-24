import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
path = "C:/Users/Caner Filiz/Desktop/Python/ispark-otoparklarna-ait-bilgiler.xlsx"
sheetName ="İSPARK Otoparklarına Ait B."
df_Ispark_saved = pd.read_excel(path, sheetName)
df_Ispark = pd.read_excel(path, sheetName)
class ISPARK():
    def __init__(self, dataFrame):
        self.__dataFrame = dataFrame
    def getCorr(self):
        Corr = self.__dataFrame.corr()
        return  Corr
    def column_split(self, columnName, splitParameter, rename1, rename2):
        new_column = self.__dataFrame[columnName].str.split(splitParameter, expand = True)
        if rename1 == False and rename2 == False:
            pass
        else:
            new_column.rename(columns = {0: rename1, 1: rename2}, inplace = True)
        return new_column
    def drop_column(self, droplist):
        __dataFrame = self.__dataFrame.drop(droplist, 1)
        return __dataFrame
    def drop_row(self, droplist):
        __dataFrame = self.__dataFrame.drop(droplist, 0)
        return __dataFrame
    def set_column_lowercase(self, column_name):
        __dataFrame = self.__dataFrame[column_name]
        return __dataFrame

# Dataframe Features
print(df_Ispark.columns)

# Dataframe Info
print(df_Ispark.info())

# Corr Map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(ISPARK(df_Ispark).getCorr(), annot=True, linewidths=.100, fmt= '.1f',ax=ax)
plt.title("Korelasyon Grafiği")
plt.show()

# -- DATA CLEANING --

# Section - 1 | Splitting -Tarifesi- Feature
featureTarifesi = ISPARK(df_Ispark).column_split("Tarifesi",";", False, False)
tarife01 = ISPARK(featureTarifesi).column_split(0, ":", "Saat01", "Ücret01")
tarife12 = ISPARK(featureTarifesi).column_split(1, ":", "Saat12", "Ücret12")
tarife24 = ISPARK(featureTarifesi).column_split(2, ":", "Saat24", "Ücret24")
tarife48 = ISPARK(featureTarifesi).column_split(3, ":", "Saat48", "Ücret48")
df_Ispark = ISPARK(df_Ispark).drop_column(['Lokasyon ID', 'Lokasyon Kodu', 'Enlem/Boylam', 'Polygon Verisi', 'Boylam', 'Enlem','Tarifesi'])
df_Ispark["Saat01"] = tarife01['Saat01'].str.lower()
df_Ispark["Ücret01"] = tarife01['Ücret01']
df_Ispark["Saat12"] = tarife12['Saat12'].str.lower()
df_Ispark["Ücret12"] = tarife12['Ücret12']
df_Ispark["Saat24"] = tarife24['Saat24'].str.lower()
df_Ispark["Ücret24"] = tarife24['Ücret24']
df_Ispark["Saat48"] = tarife48['Saat48'].str.lower()
df_Ispark["Ücret48"] = tarife48['Ücret48']


# Section - 2 | Data Preparation
def delete_spaces(dataframe):
    counter = 0
    for value in dataframe:
        value = value.replace(" ", "")
        dataframe.iloc[counter] = value
        counter += 1
    return dataframe

def delete_unwanted_rows(dataframe,feauture, wanted_value):

    list_index = list(dataframe.index)
    for i in list_index:
            if feauture[i] != wanted_value:
                dataframe = ISPARK(dataframe).drop_row(i)
            else:
                continue
    return dataframe

def convert_and_replace(dataframe):
    counter = 0
    for value in dataframe:
        value = value.replace(",", ".")
        value = float(value)
        dataframe.iloc[counter] = value
        counter += 1
    return dataframe

df_Ispark['Saat01'] = df_Ispark['Saat01'].astype(str)
df_Ispark["Saat01"] = delete_spaces(df_Ispark["Saat01"])
df_Ispark['Saat12'] = df_Ispark['Saat12'].astype(str)
df_Ispark["Saat12"] = delete_spaces(df_Ispark["Saat12"])
df_Ispark['Saat24'] = df_Ispark['Saat24'].astype(str)
df_Ispark["Saat24"] = delete_spaces(df_Ispark["Saat24"])
df_Ispark['Saat48'] = df_Ispark['Saat48'].astype(str)
df_Ispark["Saat48"] = delete_spaces(df_Ispark["Saat48"])

df_Ispark = delete_unwanted_rows(df_Ispark,df_Ispark['Saat01'], "0-1saat")
df_Ispark = delete_unwanted_rows(df_Ispark,df_Ispark['Saat12'], "1-2saat")
df_Ispark = delete_unwanted_rows(df_Ispark,df_Ispark['Saat24'], "2-4saat")
df_Ispark = delete_unwanted_rows(df_Ispark,df_Ispark['Saat48'], "4-8saat")

df_Ispark['Ücret01'] = convert_and_replace(df_Ispark['Ücret01'])
df_Ispark['Ücret12'] = convert_and_replace(df_Ispark['Ücret12'])
df_Ispark['Ücret24'] = convert_and_replace(df_Ispark['Ücret24'])
df_Ispark['Ücret48'] = convert_and_replace(df_Ispark['Ücret48'])

m_Ücret01 = df_Ispark['Ücret01'].mean()
m_Ücret12 = df_Ispark['Ücret12'].mean()
m_Ücret24 = df_Ispark['Ücret24'].mean()
m_Ücret48 = df_Ispark['Ücret48'].mean()

m_Ücret = [m_Ücret01.round(2), m_Ücret12.round(2), m_Ücret24.round(2), m_Ücret48.round(2)]
m_Saat = ['0-1 Saat', '1-2 Saat', '2-4 Saat', '4-8 Saat']
# Section - 3 | Visualization

fig = plt.figure(figsize=(15,10))
sns.barplot(x = m_Saat, y = m_Ücret, alpha = 1, palette="Blues_d")
plt.xticks(rotation = 45)
plt.xlabel('Saat Aralıkları')
plt.ylabel("Ortalama Ücret(TL)")
plt.title('SAAT ARALIKLARINA GÖRE ORTALAMA PARK ÜCRETİ GRAFİĞİ')
plt.grid(axis='y', linestyle = '-')
plt.show()





