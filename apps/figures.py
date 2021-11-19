import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import dash_daq as daq
import pandas as pd
from dash.dependencies import Input, Output
import dash_table
from wordcloud import WordCloud
# from PIL import Image
# import numpy as np
from app import app
from io import BytesIO
import base64


df = pd.read_csv('./clean_dataset.csv')
fig = px.histogram(df, x=df["total"], nbins=100)
df_numerical_column = ['unit_price', 'total', 'cogs', 'gross_income']
df_piechart_column = ['branch', 'city', 'customer_type',
                      'gender', 'payment', 'product_line']
df_figure_type = ['pie', 'bar']

df_average_rating = df.groupby('product_line')[
    'rating'].mean().sort_values().reset_index()
avg_gross_inc = df.groupby('product_line')[
    'gross_income'].mean().sort_values().reset_index()


# mask = np.array(Image.open('./assets/images/circle-shape.jpeg'))


def plot_wordcloud(data):
    text = pd.Series(df['product_line']).str.cat(sep=" ")
    wc = WordCloud(background_color="#fcf2c6").generate(text)
    return wc.to_image()


layout = html.Div(
    className="figures",
    children=[
        html.H1(
            style={'color': "#3f4e4c", 'textAlign': "center"},
            children='Display Figures',
        ),
        html.Div(
            className="figures-switch",
            children=[
                html.P(
                    "Show Table"),
                daq.BooleanSwitch(
                    id='boolean-switch-input',
                    on=True,
                    labelPosition="top",
                    color="#ebcb63"
                ),
                html.Div(id='boolean-switch-output')
            ]
        ),
        html.Div(id="empty-table", children=[]),
        html.Div(
            className="div-histogram",
            children=[
                html.H3(
                    style={'color': '#16615a'},
                    children="Numerical Histogram Graph"
                ),
                html.P(
                    children='Using graph below to have look at the reflection of value distribution in numerical column on dataset using histogram.'),
                dcc.Dropdown(
                    id="input-figure-histogram",
                    options=[
                        {'label': i, 'value': i} for i in df_numerical_column],
                    value='total',

                ),
                dcc.Graph(id="figures-histogram")
            ]
        ),
        html.Div(
            className="div-piebar",
            children=[
                html.H3(
                    style={'color': '#16615a'},
                    children="Graph For Categorical"
                ),
                html.P(
                    children='This graph using to have an insight about percentage of total value in categorial column on dataset table either using bar chart or pie chart.'),
                html.Div(
                    className="piebar-input",
                    children=[
                        dcc.Dropdown(id="input-figure-type", options=[
                            {'label': i, 'value': i}for i in df_figure_type
                        ], value='pie'),
                        dcc.Dropdown(
                            id="input-piebar-column-name",
                            options=[
                                {'label': i, 'value': i} for i in df_piechart_column
                            ],
                            value='branch'
                        ),
                    ]),
                dcc.Graph(
                    id="figures-choosen",
                )
            ]
        ),
        html.Div(
            className="div-piebar",
            children=[
                html.H3(
                    style={'color': '#16615a'},
                    children="Product Rating Graph"
                ),
                html.P(
                    children='This line graph is showing the average rate of each product.'),
                dcc.Graph(figure=px.line(
                    df_average_rating, y='rating', x='product_line', color_discrete_sequence=['red'])),
            ]
        ),

        html.Div(
            style={'marginBottom': '70px'},
            className="div-wordcloud",
            children=[
                html.H3(
                    style={'color': '#16615a'}, children="Wordcloud"
                ),
                html.P(
                    children='We can use this wordcloud chart to represent the text data in which the importance or frequency of product type (product_line column) in dataset.'),
                html.Div(
                    className="wordcloud-image",
                    children=[
                        html.Img(id="image_wc"),
                    ]
                )
            ]
        )

    ]
)


@app.callback(
    Output('empty-table', 'children'),
    Input('boolean-switch-input', 'on')
)
def toggle_show_table(value):
    if value:
        return dash_table.DataTable(
            id="df-table",
            columns=[{
                "name": i, "id": i}for i in df.columns],
            data=df.to_dict('records'),
            style_table={
                'height': '500px',
                'overflowY': 'auto',
                'overflowX': 'auto',
            },
            style_cell={'textAlign': 'left', 'padding': '15px'},
            style_header={
                'backgroundColor': '#daeeeb',
                'fontWeight': 'bold'
            },
        )
    return html.Div()


@app.callback(
    Output('boolean-switch-output', 'children'),
    Input('boolean-switch-input', 'on')
)
def update_output(on):
    if on == False:
        return "OFF"
    else:
        return "ON"


# Histogram function
@app.callback(
    Output('figures-histogram', 'figure'),
    Input('input-figure-histogram', 'value')
)
def show_histogram(value):
    return px.histogram(df, x=df[value], nbins=100, color_discrete_sequence=['#248796'])


# PieBar function
@app.callback(
    Output('figures-choosen', 'figure'),
    [Input('input-figure-type', 'value'),
     Input('input-piebar-column-name', 'value'), ]
)
def show_piebar(value1, value2):
    if value1 == 'pie':
        return px.pie(df, names=value2)
    else:
        return px.bar(data_frame=df, x=value2, color=value2,)

# Wordcloud functions


@app.callback(Output('image_wc', 'src'), [Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=df['product_line']).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())
