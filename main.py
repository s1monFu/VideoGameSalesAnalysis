from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import os

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
# 