import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Pig Latin Convertor'
initial_value='I can speak Pig Latin'
longtext='''
        _Suggestions you might try:_
        * Pig Latin is stupid
        * What is Pig Latin
        * I cannot understand pig latin
        '''
tabtitle = 'racecar'
sourceurl = 'https://en.m.wikipedia.org/wiki/Pig_Latin'
githublink = 'https://github.com/nomsdoms/dash-simple-callback/'

########### Define a function for your callback:
def my_function(letters):
words = str(letters.split())
    for word in words:
        return (word[1:] + word[0] + "ay", end = " ")

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown(longtext)]),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.Div(id='my-div'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    palin=my_function(input_value)
    return f"You've entered '{input_value}', and your output is '{palin}'"

############ Deploy
if __name__ == '__main__':
    app.run_server()
