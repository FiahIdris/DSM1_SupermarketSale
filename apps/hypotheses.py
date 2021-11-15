
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_table


df = pd.read_csv('./clean_dataset.csv')
total_sales = pd.DataFrame(df.describe()).reset_index()

layout = html.Div(
    className="hypotheses",
    children=[
        html.H1(
            style={'color': "#3f4e4c", 'textAlign': "center"},
            children='Hypothesis Testing',
        ),
        html.H4(
            style={'color': '#586967'},
            children='For t-test, we conduct single sample two tailed hypothesis testing to find out whether the average daily sales is equal to total sales column mean.'
        ),
        html.Div(
            style={'display': 'flex', 'flexDirection': 'row',
                   'justifyContent': 'space-between', 'alignItems': 'center'},
            children=[
                html.Div(
                    style={
                        'width': '60%',
                    },
                    children=[
                        html.P(
                            style={'color': '#29271d', },
                            children="Look at median of total column:"
                        ),
                        dcc.Graph(
                            figure=px.violin(
                                df, y=df['total'], orientation='v', color_discrete_sequence=['#248796'])
                        ),
                    ]),
                html.Div(
                    style={
                        'width': '35%',
                    },
                    children=[
                        html.P(
                            style={'color': '#29271d', 'marginBottom': '90px'},
                            children="Here the general description of total column:"
                        ),
                        dash_table.DataTable(
                            columns=[{
                                "name": i, "id": i}for i in ['index', 'total']],
                            data=total_sales.to_dict('records'),
                            style_table={
                                'height': '400px',
                                'overflowY': 'auto',
                                'overflowX': 'auto',
                            }
                        ), ]),
            ]),

        html.H3(
            style={'color': '#16615a'},
            children='Hypotheses Statement:'
        ),
        html.P(
            style={'color': '#29271d', },
            children="We start the test by defining two hypotheses:"
        ),
        html.Ol(
            style={'color': '#29271d'},
            children=[
                html.Li(
                    "The null hypothesis (H0) is that the average daily sales of the supermarket company is 322.96."
                ),
                html.Li(
                    "The alternative hypothesis (H1) is that the average daily sales of the supermarket company is not 322.96."
                ),

            ]
        ),
        html.Div(
            className="hypotheses-math-statement",
            children=[
                html.Div(
                    style={
                        'paddingTop': '10px',  'paddingBottom': '20px', 'textAlign': 'center', 'borderRadius': '20px'},
                    children=[
                        html.P(
                            style={'color': '#29271d'},
                            children="We can write these hyphotesis in mathematical expression as below:  "
                        ),
                        html.Img(src="/assets/math.png",
                                 style={'width': "300px", 'alignItems': 'center'}),

                    ]
                )
            ]),
        html.H3(
            style={'color': '#16615a', },
            children='Processing:'
        ),
        html.P(
            style={'color': '#29271d'},
            children="We will determine whether our null hypothesis(H0) is accepted by comparing the p-value with our confidence level or critical value. If we specify confidence level as 0.95, then our critical value will be 0.05. In this case we will determine the confidence level and our critical value as the general standar which is 0.05 for critical value and 0.95 for confidence level."
        ),
        html.Div(
            className="hypotheses-math-statement",
            children=[
                html.Div(
                    style={
                        'paddingTop': '10px',  'paddingBottom': '20px', 'textAlign': 'center', 'borderRadius': '20px'},
                    children=[
                        html.P(
                            style={'color': '#29271d', 'paddingTop': '20px', },
                            children="T-test calculation using scipy stats:"
                        ),
                        html.Img(
                            src="/assets/calculate.png", style={'width': "460px", 'height': "150px", 'textAlign': "center"}),
                        html.P(
                            style={'textAlign': 'center'},
                            children="t-statistic:0.17073034458783645"),
                        html.P("p-value:0.8644703731085056"),
                        html.P(
                            style={'color': '#29271d', 'paddingTop': '20px', },
                            children="Find out confidence interval with normal distribution:"
                        ),
                        html.Img(
                            src="/assets/display_fig.png", style={'width': "560px", 'height': "210px"}),
                        html.P(
                            style={'color': '#29271d', 'paddingTop': '20px', },
                            children="Display result:"
                        ),
                        html.Img(
                            src="/assets/result.png", style={'width': "450px", 'height': "300px"}),
                        html.P(
                            style={'color': '#29271d', },
                            children="Green line on the histogram above is the range of confidence interval, where mean is on the yellow line and the white one is the range of what we are testing. It is placed inside the confidence interval.")
                    ]
                )
            ]),


        html.H3(
            style={'color': '#16615a', },
            children='Conclusion:'
        ),
        html.P(
            style={'color': '#29271d', 'marginBottom': '100px', },
            children="Based on the test we conducted using single sample two tailed test, we can conclude that the null hypothesis (HO) is accepted because the p-value which is 0.864 is greater than the critical value of 0.05. And according to our H0 hypothesis we can said that the average daily sales of supermarket company is equal to 322.96")


    ]
)
