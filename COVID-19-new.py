# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:58:21 2020

@author: uahdh
"""
import json
import random
from urllib.request import urlopen

# storing and anaysis
import numpy as np
import pandas as pd

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as offline
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import calmap
import folium
import os

import geojson


#import webbrowser
#import pandas as pd
#import plotly.graph_objs as go
#df = pd.DataFrame({'x': [1, 2, 3],
#                   'y': [1, 3, 2],
#                   'link': ['https://google.com', 'https://bing.com', 'https://duckduckgo.com']})
#
#fig = go.FigureWidget(layout={'hovermode': 'closest'})
#scatter = fig.add_scatter(x=df.x, y=df.y, mode='markers', marker={'size': 20})
#
#def do_click(trace, points, state):
#    if points.point_inds:
#        ind = points.point_inds[0]
#        url = df.link.iloc[ind]
#        webbrowser.open_new_tab(url)
#        
#scatter.on_click(do_click)
#fig


with open('C:\Linux\Barotropic\case6\WMO_basemap.json') as f:
    gj = geojson.load(f)
features = gj['features'][30]

full_latest_grouped = pd.read_csv('GBON-HZ-new.csv')

full_latest_grouped2 = pd.read_csv('GBON-HZ_specific.csv')


#api = CovId19Data(force=False)
#
#temp = api.get_all_records_by_country()

fig = px.choropleth(full_latest_grouped,  geojson=gj, featureidkey='properties.POL_C_CODE',
                    locations="Country Code",
                    color='NMHS self assessment',
                    color_discrete_map={
#                    "Comfortable, well prepared": "#1bd1a5",
                    "Well prepared for the situation": "#00e09e",
#                    "So far under control, but a bit worried": "#4b5cc4",
                    "So far in control but worries": "#fff143",
                    "Currently impacted and concerned": "#ff4777",
                    "Survey not returned": "#fffbf0",
                    "level five": "red"},
                    category_orders={"NMHS self assessment": ["Well prepared for the situation", "So far in control but worries", "Currently impacted and concerned", "Survey not returned"]},
                    hover_name="Country", 
                    title='Second COVID-19 Impact Survey - 9 Dec - 54 Responses Received')




#fig = px.choropleth(full_latest_grouped2,  geojson=gj, featureidkey='properties.TERR_NAME',
#                    locations="TERR_NAME",
#                    color='Emergency Level',
#                    color_discrete_map={
##                    "Comfortable, well prepared": "#1bd1a5",
#                    "Comfortable, well prepared": "#00e09e",
##                    "So far under control, but a bit worried": "#4b5cc4",
#                    "So far under control, but a bit worried": "#44cef6",
#                    "Currently impacted, feeling concerned": "#ff4777",
#                    "not yet responsed": "#fffbf0",
#                    "level five": "red"},
#                    category_orders={"Emergency Level": ["Comfortable, well prepared", "So far under control, but a bit worried", "Currently impacted, feeling concerned", "not yet responsed"]},
#                    hover_name="TERR_NAME", hover_data = ['Specific requiement'],
#                    title='COVID-19 Impact Survey Analysis- updated version- 20 Apr')
#fig.update_geos(fitbounds="locations", visible=False)
fig.update(layout_coloraxis_showscale=False)
fig.show()


fig.write_html("Second COVID-19 impact mapping - new.html")

offline.init_notebook_mode()

offline.iplot(
                fig,
                filename = 'C:\Linux\Barotropic\case6\COVID',
                image = 'png',
                image_height = 32,
                image_width = 22 ,
                )


