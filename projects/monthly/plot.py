import os
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

location = os.path.dirname(os.path.abspath(__file__))

data1 = pd.read_csv(os.path.join(location, 'static/data/titanic.csv'))
data2 = pd.read_csv(os.path.join(location, 'static/data/titanic2.csv'))

def pie_plot():
    labels = ["1등실, 어린이", "2등실, 어린이", "3등실, 어린이", "1등실, 여성", "2등실, 여성",
              "3등실, 여성", "1등실, 남성", "2등실, 남성", "3등실, 남성", "승무원, 여성", "승무원, 남성"]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=data2['구조인원'], name="구조인원"),
              1, 1)
    fig.add_trace(go.Pie(labels=labels, values=data2['사망인원'], name="사망인원"),
              1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
    title_text="타이타닉호의 구조인원과 사망인원 정보",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='구조인원', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='사망인원', x=0.82, y=0.5, font_size=20, showarrow=False)])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON