import pandas 
from pandas import DataFrame

data = pandas.read_csv('lsd_math_score_data.csv')

data["high_scores"] = data["Avg_Math_Test_Score"] +100
data["high_scores"] = data["high_scores"]**2
data

columnList = ["LSD_ppm", "Avg_Math_Test_Score"] # list erstellen

cleanData = data[columnList] # liste als Schablone für neuen DataFrame benutzen
print(cleanData)
