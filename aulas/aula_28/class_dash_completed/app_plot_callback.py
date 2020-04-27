# import dash componentes
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# analise basica
import pandas as pd 
import numpy as np 

# visualização
import plotly.graph_objs as go

# instanciando o server
app = dash.Dash()

# importando os dados
df = pd.read_csv('data/gapminderDataFiveYear.csv')

# slider options
slider_min, slider_max = df['year'].min(), df['year'].max()
slider_step = 5

# layout
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(id='year-picker',
               min=slider_min,
               max=slider_max,
               step=slider_step,
               marks={int(year): str(year) for year in df['year'].unique()},
               value=slider_min)
])

# implementando o callback da figura
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='year-picker', component_property='value')])
def update_figure(selected_year):
    # slice no ano correspondente
    filtered_df = df[df['year'] == selected_year]
    
    # traces
    traces = []
    for country in filtered_df['country'].unique():
        df_by_country = filtered_df[filtered_df['country'] == country]
        traces.append(go.Scatter(
            x=df_by_country['gdpPercap'],
            y=df_by_country['lifeExp'],
            text=df_by_country['country'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=country
        ))
        
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            hovermode='closest'
        )
    }
    

if __name__ == '__main__':
    app.run_server(debug=False)
