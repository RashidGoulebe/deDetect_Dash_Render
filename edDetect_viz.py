from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('eddetect_output_advanced_clean_02.csv', sep=';')

app = Dash(__name__)

# Rander.com
server = app.server
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(df.city.unique(), 'Aachen', id='city'),
    dcc.Dropdown(['pres', 'prcp'], 'pres', id='metric'),
    dcc.Graph(id='graph-content')
])



@callback(
    Output('graph-content', 'figure'),
    Input('city', 'value'),
    Input('metric', 'value')
)
def update_graph(city,metric):

    dff = df[df.city == city]
    return px.line(dff, x='ds', y=metric)


if __name__ == '__main__':
    app.run(debug=True)
