# import dash componentes
import dash 
import dash_core_components as dcc
import dash_html_components as html

# dash app
app = dash.Dash()

# definindo cores
colors = {'background': '#282b38',
          'text': '#a5b1cd'}

# criar um layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
            style={'textAlign': 'center',
                   'color': colors['text']}),
    html.Div(children='Dash: Um framework de visualização de dados em Python',
             style={'textAlign': 'center',
                    'color': colors['text']}),
    dcc.Graph(figure={
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Classe 1'},
                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Classe 2'}],
        'layout': {'title': 'Dash Data Visualization',
                   'plot_bgcolor': colors['background'],
                   'paper_bgcolor': colors['background'],
                   'font': {'color': colors['text']}}
    })
], style={'backgroundColor': colors['background']})

if __name__=='__main__':
    app.run_server()

