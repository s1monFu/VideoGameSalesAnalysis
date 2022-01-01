from numpy import mod
from pandas.core.algorithms import mode
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_val_score
import numpy as np

# Read in data
vgSales = pd.read_csv(os.path.join("Data","vgsales.csv"))

# Find out what genre of games is most popular overall
fig, ax = plt.subplots(figsize=(6, 4))
genreSales = vgSales.groupby("Genre").sum().sort_values(
    "Global_Sales", ascending=False)
genreSales.plot.bar(ax=ax, y=["Global_Sales"], rot=45)
fig.savefig(os.path.join("Graphs", "GenreSales"), bbox_inches='tight')

# How do sales of different types of games change over time
fig2, ax2 = plt.subplots(figsize=(6, 4))
overtimeSales =vgSales[["Year","Genre","Global_Sales"]].groupby(["Genre","Year"]).sum()
overtimeSales.reset_index(level=0, inplace=True)
overtimeSales = overtimeSales.pivot(columns="Genre",values = "Global_Sales").fillna(0)
overtimeSales.plot.line(ax=ax2)
fig2.savefig(os.path.join("Graphs","OvertimeSales"),bbox_inches='tight')

# A linear regression model for sale prediction
train,test = train_test_split(vgSales)
model = Pipeline([
            ("transformer",make_column_transformer((OneHotEncoder(),["Genre","Platform"]))),
            ("linear",LinearRegression())
        ])
scores = cross_val_score(model,train[["Genre","Platform","Year"]],train["Global_Sales"],cv=10)
scores = scores[~np.isnan(scores)]
print(scores.mean())
