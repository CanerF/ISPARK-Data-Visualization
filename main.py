import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
path = "C:/Users/Caner Filiz/Desktop/Python/ispark-otoparklarna-ait-bilgiler.xlsx"
sheetName ="İSPARK Otoparklarına Ait B."
df_Ispark = pd.read_excel(path, sheetName)
class ISPARK():
    def __init__(self, dataFrame):
        self.__dataFrame = dataFrame
    def getColumns(self):
        Features = self.__dataFrame.columns
        return Features
    def getInfo(self):
        Info = self.__dataFrame.info()
        return Info
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
        __dataFrame = self.__dataFrame[column_name].str.lower()
        return __dataFrame

# Dataframe Features
print(ISPARK(df_Ispark).getColumns())

# Dataframe Info
print(ISPARK(df_Ispark).getInfo())

# Corr Map
#f,ax = plt.subplots(figsize=(18, 18))
#sns.heatmap(ISPARK(df_Ispark).getCorr(), annot=True, linewidths=.100, fmt= '.1f',ax=ax)
#plt.title("Correlation Chart")
#plt.show()

# DATA CLEANING

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



#def drop_unwanted_rows(dataframe, wanted_feature, wanted_value, wanted_value2):
#    indexNames = list(dataframe.index.values)
#    counter = 0
#    wanted_value += "  "
#    for i in df_Ispark[wanted_feature]:
#        if i != wanted_value or i != wanted_value2 and counter == indexNames[counter]:
#            dataframe = dataframe.drop(counter)
#            counter += 1
#        else:
#            counter += 1
#    return dataframe

#df_Ispark = drop_unwanted_rows(df_Ispark,"Saat01", "0-1 Saat","0-1 saat")
#df_Ispark = drop_unwanted_rows(df_Ispark,"Saat12", "1-2 Saat","1-2 saat")
#df_Ispark = drop_unwanted_rows(df_Ispark,"Saat24", "2-4 Saat","2-4 saat")
#df_Ispark = drop_unwanted_rows(df_Ispark,"Saat48", "4-8 Saat","4-8 saat")
















