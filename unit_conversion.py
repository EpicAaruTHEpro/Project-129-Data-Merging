import pandas as pd
import csv

df = pd.read_csv("brown_dwarfs_stars.csv")
# Drops column values that are NaN
df = df.dropna()
# Converts to solar radius and solar mass
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
# Creates new csv
df.to_csv("unit_converted_stars.csv")