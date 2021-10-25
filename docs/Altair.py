#!/usr/bin/env python
# coding: utf-8


import altair as alt 
import pandas as pd 
import numpy as np
import os
import altair_viewer
plugs_df = pd.read_csv('plugs_output.csv')





plugs_df = pd.read_csv('plugs_output.csv')

alt.data_transformers.disable_max_rows()

plugs_df['House'] = plugs_df['House'].astype('category')
plugs_df['Total'] = plugs_df['Fridge'] + plugs_df['Entertainment']
plugs_df['period'] = pd.to_datetime(plugs_df['period'])
plugs_df['month'] = plugs_df['period'].dt.month

select_month = alt.selection_single(
    name = 'select',fields = ['month'],init = {'month':1},
    bind = alt.binding_range(min = 1, max = 12, step = 1)
)
final_chart =alt.Chart(plugs_df).mark_point(filled=True).encode(
    alt.X('Fridge', scale=alt.Scale(zero=False)),
    alt.Y('Entertainment', scale=alt.Scale(zero=False)),
    alt.Size('Total:Q'),
    alt.Color('House:N'),
    alt.Order('Total:Q', sort='descending'),
    
).add_selection(select_month).transform_filter(select_month).properties(title = 'Comparison between Fridge and Entertainment')



alt.renderers.enable('altair_viewer')
final_chart.save('altair.html')

