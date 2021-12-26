from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read in data
vgSales = pd.read_csv(os.path.join("Data","vgsales.csv"))
fig, ax = plt.subplots(figsize=(6, 4))

# Find out what genre of games is most popular overall
genreSales = vgSales.groupby("Genre").sum().sort_values(
    "Global_Sales", ascending=False)
genreSales.plot.bar(ax=ax, y=["Global_Sales"], rot=45)
fig.savefig(os.path.join("Graphs", "GenreSales"), bbox_inches='tight')

# How do sales of different types of games change over time

# 