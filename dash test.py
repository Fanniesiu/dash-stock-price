import pandas_datareader.data as web
import datetime
import fix_yahoo_finance as yf 
import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash()

stock = 'TSLA'
yf.pdr_override()
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.get_data_yahoo('TSLA', start, end)
df.reset_index("Date", inplace=True)

app.layout = html.Div(children=[
    html.H1(children='STOCK PRICE SAMPLE', style={
        'textAlign':'center',
        'color':'black'
        }),

    html.Div(children='Stock Price Data from Yahoo Finance', style={
        'textAlign':'center',
        'color':'#bbbbbb'
        }

        ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x':df.Date, 'y':df.Close, 'type':'line','name':stock},
            ],
        'layout':{
            'title':stock
                }
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)



