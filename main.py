from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import os
vgSales = pd.read_csv(os.path.join("vgsales.csv"))

# Find out what genre of games is most popular
fig, ax = plt.subplots(figsize=(6,4))
genreSales = vgSales.groupby("Genre").sum().sort_values("Global_Sales",ascending=False)
genreSales.plot.bar(ax=ax,y=["Global_Sales"])
fig.savefig(os.path.join("Graphs","GenreGraph"))