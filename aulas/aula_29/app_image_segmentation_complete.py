
# dash imports
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

# image convert
import base64
from PIL import Image
import io

# plotly
import plotly.express as px

# scientific
import numpy as np
from sklearn.cluster import KMeans

# stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# colors
colors = {'background': '#282b38',
          'text': '#a5b1cd'}

# app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Color segmentation"

# layout
app.layout = html.Div([
    html.Div([
        html.H2("KMeans segmentation"),
        html.Div([
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Image')
                    ]),
            style={
                'width': '90%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
                })
              ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(id='choose-k',
                         options=[{'label': str(i), 'value': i} for i in range(1, 11)],
                         value=1)], 
                 style={'width': '10%',
                        'display': 'inline-block',
                        'vertical-align': 'top',
                        'margin': '10px'}),
        html.Div([
            html.Button(id='submit-button',
                        n_clicks=0,
                        children='Submit')], 
                 style={'width': '20%',
                        'display': 'inline-block',
                        'vertical-align': 'top',
                        'margin': '10px',
                        'color': colors['text']})
        ]),
    html.Div([
        html.Div(
            dcc.Loading(html.Div(id='output-image-upload-raw'),
                        style={'position': 'fixed', 'top': '50%'}), 
            style={'width': '50%',
                   'display': 'inline-block',
                   'height': '100%',
                   'vertical-align': 'middle'}),
        html.Div(
            dcc.Loading(html.Div(id='output-image-upload-kmeans'),
                        style={'position': 'fixed', 'top': '50%'}),
            style={'width': '50%',
                   'display': 'inline-block',
                   'height': '100%',
                   'vertical-align': 'middle'})
        ], style={'height': '500px'})
    ], style={'backgroundColor': colors['background'],
              'color': colors['text']})

@app.callback([Output('output-image-upload-raw', 'children'),
               Output('output-image-upload-kmeans', 'children')],
              [Input('submit-button', 'n_clicks')],
              [State('upload-image', 'contents'),
               State('choose-k', 'value')])
def segment_image(_, image, k: int):
    """ Callback that applies image segmentation and displays result.
    
    Args:
        _ : button input ignored.
        image: input image.
        k (int): number of clusters.
    
    Returns:
        raw_plot: original image plot.
        kmeans_plot: segmented image plot.
    """    
    # convert raw input image to RGB numpy
    img = stringToRGB(image)
    raw_fig = px.imshow(img)
    raw_fig.update_xaxes(showticklabels=False)
    raw_fig.update_layout(plot_bgcolor=colors['background'],
                          paper_bgcolor=colors['background'])
    raw_fig.update_yaxes(showticklabels=False)
    raw_fig.update_traces(hovertemplate=None, hoverinfo='skip')
    
    # display raw image
    raw_plot = html.Div([html.H3("Raw image: "),
                           dcc.Graph(figure=raw_fig)])

    # image kmeans
    img_kmeans = cluster_image(img, k)

    # kmeans fig
    seg_fig = px.imshow(img_kmeans)
    seg_fig.update_xaxes(showticklabels=False)
    seg_fig.update_yaxes(showticklabels=False)
    seg_fig.update_layout(plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'])
    seg_fig.update_traces(hovertemplate=None, hoverinfo='skip')
    
    # display segmented image
    kmeans_plot = html.Div([html.H3("Segmented image: "),
                           dcc.Graph(figure=seg_fig)])

    return raw_plot, kmeans_plot

def cluster_image(img: np.ndarray, k: int):
    """Apply kmeans to image.
    
    Args:
        img (np.ndarray): input image.
        k (int): number of clusters.
    
    Returns:
        img_kmeans (np.ndarray): segmented image.
    """    
    # convert to float32
    X = img.reshape((-1,3))
    X = np.float32(X)

    # fit kmeans
    kmeans = KMeans(n_clusters = k, init = 'k-means++', random_state = 0, n_jobs=-1)
    kmeans.fit(X)

    # parameters
    label, center = kmeans.labels_, kmeans.cluster_centers_

    # now convert back into uint8, and make original image
    center = np.uint8(center)
    img_kmeans = center[label.flatten()]
    img_kmeans = img_kmeans.reshape((img.shape))

    return img_kmeans

def stringToRGB(base64_string):
    """Converts base64 input image to RGB numpy.
    
    Args:
        base64_string (base64): input image.
    
    Returns:
        img (np.ndarray): RGB image. 
    """    
    url = base64_string.split(',')
    image = Image.open(io.BytesIO(base64.b64decode(url[-1])))
    image = image.convert('RGB')
    return np.array(image)

if __name__ == '__main__':
    app.run_server(debug=False)
