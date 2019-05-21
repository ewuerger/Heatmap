# Get this figure: fig = py.get_figure("https://plot.ly/~cufflinks/92/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~cufflinks/92/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="simple-heatmap", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~cufflinks/92/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

M = []
def generate_Heatmap():
    py.sign_in('Wuerger', 't4iqJstmPhnps98v2ZbK')
    trace1 = {"z": M,
              "colorbar": {"ticklen": 2, "title": ""},
              "colorscale": [[0, "rgb(0,0,155)"], [0.35, "rgb(0,108,255)"], [0.5, "rgb(98,255,146)"],
                             [0.6, "rgb(255,147,0)"], [0.7, "rgb(255,47,0)"], [1, "rgb(216,0,0)"]],
              "opacity": 0.5, "showscale": True, "type": "heatmap", "uid": "264e0c", "xaxis": "x", "yaxis": "y",
              "zauto": True, "zsmooth": "best"}
    data = Data([trace1])
    layout = {"margin": {"r": 10, "t": 25, "b": 40, "l": 60}, "showlegend": False, "xaxis": {"domain": [0, 1]},
              "yaxis": {"domain": [0, 1]}}
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
    return plot_url