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
confirm = pd.read_csv('data/confirm.csv')
recover = pd.read_csv('data/recover.csv')
death = pd.read_csv('data/death.csv')

# confirm = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
# recover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
# death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')

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

def mergeData(x,recover,death):
    """
    Function that merge the confirm, recover and death to one dataframe
    """
    x = x.rename(columns = {'latest':'confirm'})
    x['recover'] = recover['latest']
    x['death'] = death['latest']

    return x


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
Abdul Jalal Mohammed🇬🇭,
John Bagiliko🇬🇭
"""

line = go.Figure()
#***************************************************************************
# Graph
confirm_line_data = confirm.iloc[:,5:].sum()
recover_line_data = recover.iloc[:,5:].sum()
death_line_data = death.iloc[:,5:].sum()

line.add_trace(
    go.Scatter(
        x = confirm_line_data.index,
        y = confirm_line_data.values,
        text=confirm_line_data.values,
        hoverinfo='text',
        mode = 'lines',
        line = dict(
            color = 'rgb(255, 103, 0)',
            width=2,)
    ),
)
line.add_trace(
    go.Scatter(
        x = recover_line_data.index,
        y = recover_line_data.values,
        mode = 'lines',
        text=recover_line_data.values,
        hoverinfo='text',
        line = dict(
            color = 'rgb(0, 128, 0)',
            width=2,)
    )
)
line.add_trace(
    go.Scatter(
        x = death_line_data.index,
        y = death_line_data.values,
        mode = 'lines',
        text=death_line_data.values,
        hoverinfo='text',
        line = dict(
            color = 'rgb(255, 0, 0)',
            width=2,)
    )
)

line.update_layout(
    xaxis=dict(
        showline=False,
        showgrid=False,
        zeroline=False,
        showticklabels=False,
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    height=150,
    autosize=True,
    margin=dict(
        # autoexpand=False,
        l=0,
        r=0,
        t=0,
        b=0
    ),
    showlegend=False,
    plot_bgcolor='white'
)


#****************************************************************************
# Merged data
get_merged = mergeData(get_confirm, get_recover, get_death)

limits = [(1,10), (10,100), (100,1000), (1000,10000), (10000,1000000000)]
size = [5, 10, 15, 20, 30]

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    get_confirm_range = get_merged[get_merged['confirm']>=lim[0]]
    get_confirm_range = get_confirm_range[get_confirm_range['confirm']<lim[1]]

    customdata=np.dstack((get_confirm_range['confirm'], get_confirm_range['recover']))

    figMap = fig.add_trace(
            go.Scattergeo(
            lon = get_confirm_range['Long'],
            lat = get_confirm_range['Lat'],
            text = get_confirm_range['Country/Region'],
            mode = 'markers',
            showlegend=False,
            marker = dict(
                size = size[i],
                color = 'rgba(255, 103, 0,0.5)',
                sizemode = 'area'
            ),
            customdata=get_confirm_range['confirm'],
            # hovertext=[get_confirm_range['Country/Region'],get_confirm_range['confirm'],get_confirm_range['recover'],get_confirm_range['death']]
            hovertemplate = "<b>%{text}</b>,<br>Confirm:%{customdata}<extra></extra><br>",
            # # trace=off
            # hoverinfo='text'
        ),
    )
figMap.update_layout(
    autosize=True,
    margin={
        "r":0,
        "t":0,
        "l":0,
        "b":0,
    },
    height=330,
    # width=700,
    geo = go.layout.Geo(
        resolution = 50,
        showframe = False,
        showcoastlines = True,
        showcountries = True,
        landcolor = "rgb(229, 229, 229)",
        countrycolor = "white" ,
        projection = dict(scale=1.8),
        coastlinecolor = "white",
        center= dict(
            lat= 8.7832,
            lon= 20.5085,
        )
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
                # Graph
                html.P(['Graph'], className='title container'),
                dcc.Graph(
                    id='lineGraph',
                    figure = line,
                    className=''
                ),
            ], className='graph card'),   
            
        ], className='col-12 col-md-2'),

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

            # Sponsor
            html.Div([
                html.P(['Sponsor'], className='title'),
            ], className='report card container'),
        ], className='col-12 col-md-6'),

        # Column 3
        html.Div([
            # News
            # html.Div([
            #     html.P(['News'], className='title'),
            # ], className='news card container'),

            # Tweet
            html.Div([
                html.P(['Tweets'], className='title'),
            ], className='news card container'),

            # Contributors
            html.Div([
                html.P(['Contributors'], className='title'),
                html.P(contributor, className='contributor')
            ], className='report card container'),
        ], className='col-12 col-md-4'),
    ], className='row allColumns main')
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