import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Pig Latin Convertor'
initial_value='Pig Latin is fun'
longtext='''
        _Suggestions you might try:_
        * Pig Latin is not fun
        * Can I speak regular English
        * What is Pig Latin
        '''
tabtitle = 'Pig Latin'
sourceurl = 'https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/'
githublink = 'https://github.com/nomsdoms/dash-simple-callback/'

########### Define a function for your callback:
VOWELS = 'AaEeIiOoUuYy'
def my_function(sentence):
    pig_list = []
    for word in sentence.split():
        if word[0] in VOWELS:
            pig_list.append(word.lower() + "way")
        else:
            pig_list.append(word.lower()[1:] + word.lower()[0] + "ay")
    return " ".join(pig_list)

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
