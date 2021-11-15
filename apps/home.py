import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_table as dt
from collections import OrderedDict

data_election = OrderedDict(
    [
        (
            "Parameter",
            [
                "Invoice id",
                "Branch",
                "City",
                "Gender",
                "Product line",
                "Unit price",
                "Quantity",
                "Tax",
                "Total",
                "Date",
                "Time",
                "Payment",
                "COGS",
                "Gross margin percentage",
                "Gross income",
                "Rating",
            ],
        ),
        (
            "Defenition",
            ["Computer generated sales slip invoice identification number", "Branch of supercenter (3 branches are available identified by A, B and C)", "Location of supercenters", "Gender type of customer", "General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel", "Price of each product in $", "Number of products purchased by customer",
             "5% tax fee for customer buying", "Total price including tax", "Date of purchase (Record available from January 2019 to March 2019)", "Purchase time (10am to 9pm)", "Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)", "Cost of goods sold", "Gross margin percentage", "Gross income", "Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)"],
        ),
    ]
)
df = pd.DataFrame(data_election)

layout = html.Div(
    className="home",
    children=[
        html.H1(
            style={'color': "#3f4e4c", 'textAlign': "center"},
            children='Supermarket Sales Analysis',
        ),
        html.Div(className="home", children=[
            html.H3(

                style={'color': '#16615a'},
                children='Introduction',
            ),
            html.P(
                "The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data."
            )
        ]),
        html.Div(
            className="home",
            children=[
                html.H3(

                    style={'color': '#16615a'},
                    children='Attributes Information',
                ),
                dt.DataTable(
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'lineHeight': '15px'
                    },
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns],
                    style_cell={'textAlign': 'left', 'padding': '7px'},
                    style_header={
                        'backgroundColor': '#daeeeb',
                        'fontWeight': 'bold'
                    },
                )]
        ),
        html.Div(
            className="home",
            children=[
                html.H3(

                    style={'color': '#16615a'},
                    children='Objectives',
                ),
                html.P(
                    "This interactive dashboard exist to find out the answers of this following questions:"),
                html.Ul(
                    style={'marginBottom': '100px', },
                    children=[
                        html.Li(
                            "Which branch has the most sale."
                        ),
                        html.Li(
                            "Which gender make purchases more often."
                        ),
                        html.Li(
                            "What is the average total sale per month."
                        ),
                        html.Li(
                            "Which product line receive the highest rating."
                        ),
                        html.Li(
                            "Single sample two tailed hypothesis testing"
                        ),
                    ]
                )
            ]
        )


    ]
)
