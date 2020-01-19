import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
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

# Dataframe Features
print(ISPARK(df_Ispark).getColumns())

# Dataframe Info
print(ISPARK(df_Ispark).getInfo())

# Corr Map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(ISPARK(df_Ispark).getCorr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.title("Correlation Chart")
plt.show()



