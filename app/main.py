import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
import datetime
import pandas as pd
import numpy as np
from flask import Flask
from geopy.geocoders import Nominatim
import time

# Get data
confirm = pd.read_csv('../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
recover = pd.read_csv('../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
death = pd.read_csv('../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')

# Define functions



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css','https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.title='Virdash'

app.layout = html.Div([
    # Meta data
    html.Meta(
        name='viewport',
        content='width=device-width, initial-scale=1.0'),
    html.Link(
        rel='shortcut icon',
        href='https://raw.githubusercontent.com/virdash/coronavirus/master/app/assets/favicon.ico'),
    # Navigation section
    html.Div([
        html.H3('Virdash'),
    ], className='banner'),

    html.Div([])
])

if __name__ == '__main__':
    app.run_server(debug=True)