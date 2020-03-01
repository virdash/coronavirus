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

# ***********************************************************************************
# Define functions

def getLatest(df):
    """
    This get the data of the last day from the dataframe and append it to the details
    """
    df_info = df.ix[:,0:4]
    df_last = df.ix[:,-1]
    df_info['latest'] = df_last
    
    return df_info

def total_card(df):
    '''
    Total Confirmed
    '''
    latest = getLatest(df)
    return "{:,.0f}".format(latest['latest'].sum())

# ***********************************************************************************
# Sending data to view
total_confirmed = total_card(confirm)
total_recovered = total_card(recover)
total_death = total_card(death)

contributor = """
Solomon Igori🇳🇬,
Bright Morkli🇬🇭,
Ehigiator Klinton🇳🇬,
Gabriel Addo🇬🇭,
Boris Bizo🇬🇦,
Robin Mawsime🇬🇭,
Daouda Tandiang DJIBA🇸🇳,
Abdul Jalal Mohammed🇬🇭
"""

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

external_scripts = ['https://platform.twitter.com/widgets.js']
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
        id='i tire o',
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
                'Map'
            ], className='map card'),

            # Report a case
            html.Div([
                html.P(['Report a Case'], className='title'),
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



if __name__ == '__main__':
    app.run_server(debug=True)