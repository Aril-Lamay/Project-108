import csv
import plotly.figure_factory as pff
import pandas as pd

df = pd.read_csv("Project-108/data.csv")

rating = df["Avg Rating"].tolist()

figure = pff.create_distplot([rating],["Average Rating"], show_hist= False)
figure.show()