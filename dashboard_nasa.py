import dash
from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import requests
from dash.dependencies import Input, Output
from dash import dcc

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

def get_data(api_key) :
#from api_nasa import get_data
    apod_url=f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(apod_url)
    data = response.json()
    return data

style = {
    "textAlign": "center",
    "padding": "50px",
} 

app = dash.Dash(__name__)
server = app.server

app.layout = dmc.Grid(
    [
        dcc.Interval(id='interval-component', interval=60 * 1000),
        dmc.Col(
            [
                dmc.Title(id='title', align='center', size="h1"),
                dmc.Text(id='author', align='center', size="xl"),
                html.Img(id='image', style={'padding': '10px 10px 10px', 'margin': 'auto', "margin": "20px"}),
                dmc.Text(id='date', size="30px",weight=700),
                dmc.Text(id='explanation', size="30px")
            ],
            style=style
        )
    ],
    mb=100
)


@app.callback(
    [Output('title', 'children'),
     Output('author', 'children'),
     Output('date', 'children'),
     Output('image', 'src'),
     Output('explanation', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_data(n) :
    data = get_data("vR6zZ6UJloYcfESKfP2mpWKpZZ1wKqli8NW5BhwQ")
    image_url= data['url']
    date= data['date']
    explanation= data["explanation"]
    title= data["title"]
    author= data["copyright"]
    return title,date, f"The author of today's image is {author}", image_url, explanation

@app.callback(dash.dependencies.Output('interval-component', 'interval'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])

def update_layout(n):
    return 60 * 1000  # Intervalles en millisecondes

if __name__ == '__main__':
    app.run_server(debug=True)
