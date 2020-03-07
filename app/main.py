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
import requests
from geopy.geocoders import Nominatim
import time

# Get data
confirm = pd.read_csv('./data/confirm.csv')
recover = pd.read_csv('./data/recover.csv')
death = pd.read_csv('./data/death.csv')

# ***********************************************************************************
# Define functions

def getLatest(df):
    """
    This get the data of the last day from the dataframe and append it to the details
    """
    df_info = df.iloc[:,0:5]
    df_last = df.iloc[:,-1]
    df_info['latest'] = df_last
    
    return df_info

def total_card(df):
    '''
    Total Confirmed
    '''
    # latest = getLatest(df)
    return "{:,.0f}".format(df['latest'].sum())

def display_ip():
    """
    Function To Print GeoIP Latitude & Longitude
    """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})



# ***********************************************************************************
# Get latest data
get_confirm = getLatest(confirm)
get_recover = getLatest(recover)
get_death = getLatest(death)

# Sending data to view
total_confirmed = total_card(get_confirm)
total_recovered = total_card(get_recover)
total_death = total_card(get_death)

contributor = """
Solomon Igori🇳🇬,
Bright Morkli🇬🇭,
Ehigiator Klinton🇳🇬,
Gabriel Addo🇬🇭,
Boris Bizo🇬🇦,
Mawusime Aglago🇬🇭,
Daouda Tandiang DJIBA🇸🇳,
Abdul Jalal Mohammed🇬🇭
"""


figMap = go.Figure(
    data = [
            go.Scattergeo(
            lon = get_confirm['Long'],
            lat = get_confirm['Lat'],
            text = get_confirm['Country/Region'],
            mode = 'markers',
            showlegend=False,
            marker = dict(
                size = 5,
                color = 'rgba(255,0,0,0.5)',
                sizemode = 'area'
            ),
        ),
            go.Scattergeo(
            lon = get_confirm['Long'],
            lat = get_confirm['Lat'],
            text = get_confirm['Country/Region'],
            mode = 'markers',
            showlegend=False,
            marker = dict(
                size = get_confirm['latest']/1000,
                color = 'rgba(255,0,0,0.5)',
            ),
        ),
    ]
)
figMap.update_layout(
    autosize=True,
    margin={
        "r":0,
        "t":0,
        "l":0,
        "b":0,
    },
    height=280,
    # width=700,
    geo = go.layout.Geo(
        resolution = 50,
        showframe = False,
        showcoastlines = True,
        showcountries = True,
        landcolor = "rgb(229, 229, 229)",
        countrycolor = "white" ,
        projection = dict(scale=1),
        coastlinecolor = "white",
    ),
    # legend_traceorder = 'reversed'
)



external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

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
    html.Script(
        id='twitter',
        src='https://platform.twitter.com/widgets.js'),

    # Header section
    html.Div([
        html.Div([
            html.H2('Virdash'),
        ], className='container')
    ], className='banner'),

    html.Div([
        # column 1
        html.Div([
            # Confirmed card
            html.Div([
                html.P(['Total Confirmed'], className='title'),
                html.H3(total_confirmed, className='confirm value')
            ], className='total card container'),

            # Recovery card
            html.Div([
                html.P(['Total Recovered'], className='title'),
                html.H3(total_recovered, className='recover value')
            ], className='total card container'),

            # Death card
            html.Div([
                html.P(['Total Death'], className='title'),
                html.H3(total_death, className='death value')
            ], className='total card container'),


            # Graph card
            html.Div([
                'Graph'
            ], className='graph card'),
        ], className='col-2'),

        # Column 2
        html.Div([
            # Map
            html.Div([
                # Map
                dcc.Graph(
                    id='map',
                    figure = figMap,
                    className='world'
                ),
            ], className='map card'),

            # Report a case
            html.Div([
                html.P(['Report a Case'], className='title'),
                html.Button('Suspected Case', id='button'),
            ], className='report card container'),

            # Contributors
            html.Div([
                html.P(['Contributors'], className='title'),
                html.P(contributor, className='contributor')
            ], className='report card container'),
        ], className='col-5'),

        # Column 3
        html.Div([
            # News
            html.Div([
                html.P(['News'], className='title'),
            ], className='news card container'),

            # Tweet
            html.Div([
                html.P(['Tweets'], className='title'),
            ], className='news card container'),

            # Sponsor
            html.Div([
                html.P(['Sponsor'], className='title'),
            ], className='report card container'),
        ], className='col-4'),
    ], className='row allColumns')

])

# @app.callback(
#     dash.dependencies.Output('output-container-button', 'children'),
#     [dash.dependencies.Input('button', 'n_clicks')],
# )
# def update_output(n_clicks):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )

if __name__ == '__main__':
    app.run_server(debug=True)