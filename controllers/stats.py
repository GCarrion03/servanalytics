'''
Created on Oct 2, 2016

@author: Jorge Pantoja
'''

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.plotly as py

py.sign_in('georgepm', 'q0y1y77p78')

trace1 = go.Scatter(x=[1,2,3], y=[4,5,6], marker={'color': 'red', 'symbol': 104, 'size': "10"}, 
                    mode="markers+lines",  text=["one","two","three"], name='1st Trace')
                                               
data=go.Data([trace1])
layout=go.Layout(title="First Plot", xaxis={'title':'x1'}, yaxis={'title':'x2'})
figure=go.Figure(data=data,layout=layout)
py.plot(figure, filename='pyguide_1')