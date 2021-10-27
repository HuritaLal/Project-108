import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")
avgRating = data["Avg Rating"].tolist()

graph = ff.create_distplot([avgRating],["Results"],show_hist=False)
graph.show()