#Followed through the Dash Documentation: https://dash.plot.ly/getting-started

import dash
import dash_html_components as html
import flask
import sqlite3 
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly

#initalise database, Flask server and Dash application
dbname = '/home/pi/A1/sHat.db'
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashapp/')

#set up dash layout
app.layout = html.Div(children=[
    html.H1(children='Raspberry Pi Data '),

    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,
        n_intervals=0
    )
])

#set up dash graph update, extract data from database, populate graphs and display both data sets in their own
#lyouts and colours.
@app.callback(Output('live-update-graph', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph(n):
    data = {
        'datetime':[],
        'temp': [], 
        'humidity': []
    }
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        data['datetime'].append(str(row[0]))
        data['temp'].append(row[1])
        data['humidity'].append(row[2])

    fig = plotly.tools.make_subplots(rows=2,cols=1,vertical_spacing=0.2)

    fig.append_trace({
        'x':data['datetime'],
        'y':data['temp'],
        'name':'Temperature',
        'mode':'lines+markers',
        'type': 'scatter'
    }, 1,1)

    fig.append_trace({
        'x':data['datetime'],
        'y':data['humidity'],
        'name':'Humidity',
      	'mode':'lines+markers',
        'type': 'scatter'
    }, 2,1)

    return fig

#basic root web page
@server.route('/')
def index():
    return '''
<html>
<div>
    <a href="/dashapp/">Raspberry Pi Graph</a>
</div>
</html>
'''

#execute program
if __name__ == '__main__':
    server.run(host= '0.0.0.0', port= 5000, debug=True)