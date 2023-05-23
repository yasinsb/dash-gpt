# imports 

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from jupyter_dash import JupyterDash


# define the app for web page view
app = JupyterDash(__name__)


# define the layout
app.layout = html.Div([
    html.H1('Title', style={'textAlign': 'center'}),
    html.Div([
        dcc.Textarea(
            id='instruction-textbox',
            placeholder='Please type your message in the box below the page.',
            #make this text non-editable
            contentEditable=False,
            style={'width': '100%'}
        )
    ], style={'width': '30%', 'margin': 'auto'}),

    # create a div with a text box that its content will be updated after clicking the button
    # the content could be long text, so we use a text area with a scroll bar
    html.Div([
        dcc.Textarea(
            id='text-box',
            placeholder='This is a text area',
            value='',
            contentEditable=False,
            style={'width': '100%', 'height': 300, 'overflowY': 'scroll'}
        )
    ], style={'width': '70%', 'margin': 'auto'}
    ),
    # create a input text box and a submit button on its right side
    html.Div([
        dcc.Input(id='input-box', type='text', value=''),
        html.Button('Submit', id='submit-button', n_clicks=0)
    ], style={'width': '70%', 'margin': 'auto', 'marginTop': '10px', 'align': 'center', })
],
style={'width': '100%', 'margin': 'auto', 'backgroundColor': '#f2f2f2'}
)

# create a callback function to update the text box content by adding the input text to it
# with every submit click input text will be added to the text box
# and the input box will be cleaned
@app.callback(
    Output('text-box', 'value'),
    [Input('submit-button', 'n_clicks')],
    [State('input-box', 'value'),
        State('text-box', 'value')])
def update_output(n_clicks, input_value, text_box_value):
    if n_clicks > 0:
        return text_box_value + '\n' + input_value
    else:
        return text_box_value
# define another function to response to same call back and cleans the input box
@app.callback(
    Output('input-box', 'value'),
    [Input('submit-button', 'n_clicks')])
def clean_input_box(n_clicks):
    if n_clicks > 0:
        return ''
    else:
        return ''
    
if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
