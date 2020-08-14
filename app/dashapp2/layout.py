import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Amazon', 'value': 'AMZN'},
            {'label': 'FitBit', 'value': 'FIT'},
            {'label': 'Microsoft', 'value': 'MSFT'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})
