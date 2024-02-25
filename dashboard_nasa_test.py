import dash
from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import requests
from dash.dependencies import Input, Output
from dash import dcc
import datetime

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

def get_data(api_key):
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(apod_url)
    data = response.json()
    return data

style = {
    "textAlign": "center",
    "padding": "50px",
}

app.layout = dmc.Grid(
    [
        dcc.Interval(id='interval-component', interval=60 * 1000),
        dmc.Col(
            [
                dmc.Title(id='title', align='center', size="h1"),
                dmc.Text(id='author', align='center', size="xl"),
                html.Img(id='image', style={'padding': '10px 10px 10px', 'margin': 'auto', "margin": "20px"}),
                dmc.Text(id='date', size="30px"),
                dmc.Text(id='explanation', size="30px"),
                dmc.Text(id='time-left', size="20px", style={'margin-top': '20px'})
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
     Output('explanation', 'children'),
     Output('time-left', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_data(n):
    try:
        data = get_data("vR6zZ6UJloYcfESKfP2mpWKpZZ1wKqli8NW5BhwQ")
        
        # Ajoutez une vérification pour s'assurer que 'data' n'est pas None
        if data is None:
            raise ValueError("No data received from API")
        
        image_url = data.get('url', '')
        date = data.get('date', '')
        explanation = data.get("explanation", '')
        title = data.get("title", '')
        author = data.get("copyright", '')
        
        # Calculer le temps restant avant la prochaine actualisation
        time_left = datetime.timedelta(milliseconds=(60 * 1000 - (n % (60 * 1000))))
        time_left_str = f"Next update in: {time_left.seconds // 60} minutes and {time_left.seconds % 60} seconds"
        
        return title, date, f"The author of today's image is {author}", image_url, explanation, time_left_str
    except Exception as e:
        return f"Error: {str(e)}", "", "", "", "", ""