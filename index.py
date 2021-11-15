
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import home, figures, hypotheses

colors = {
    'background': '#e7f0e4',
    'text': '#7FDBFF'
}

app.layout = html.Div(className="body", children=[
    html.Div(
        className="header",
        children=[
            dcc.Link(
                href="/",
                children=[
                    html.Img(
                        src="./assets/home.png")
                ]
            ),
            html.Div(
                className="header-nav",
                children=[
                    dcc.Link('FIGURES', href="/apps/figures"),
                    dcc.Link('HYPOTHESIS', href="/apps/hypotheses")
                ]
            )
        ]
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id="page-content", children=[])
])


@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    if pathname == '/apps/figures':
        return figures.layout
    if pathname == '/apps/hypotheses':
        return hypotheses.layout

    return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
