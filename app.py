import os

import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    [
        html.H2("Hello World"),
        dcc.Dropdown(["LA", "NYC", "MTL"], "LA", id="dropdown"),
        html.Div(id="display-value"),
    ]
)


@app.callback(
    Output("display-value", "children"), [Input("dropdown", "value")]
)
def display_value(value):
    return f"You have selected {value}"


app.layout = html.Div(
    [
        html.H4("Color selection using plotly"),
        html.P("Select color:"),
        dcc.Dropdown(
            id="dropdown",
            options=["Gold", "MediumTurquoise", "LightGreen"],
            value="Gold",
            clearable=False,
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(Output("graph", "figure"), Input("dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(
            y=[2, 3, 1],  # replace with your own data source
            marker_color=color,
        )
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
