'''
data = open('data.tsv','r').read()
data = data.replace(',','').replace('\t',',')
open('data.csv','w').write(data)
'''

import os

import matplotlib.pyplot as plt
import pandas as pd
import geopandas
import mapclassify
from pycountry_convert import country_name_to_country_alpha3


datafile = 'data.csv'
shapefile = '../ne_10m_admin_0_countries_lakes.shp'

cols = ['Country', 'Salary (USD)']

df = pd.read_csv(datafile, names=cols)
df['Country'] = [country_name_to_country_alpha3(x) for x in df['Country']]

gdf = geopandas.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')

df = gdf.merge(df, left_on='ADM0_A3', right_on='Country')

ax = df.dropna().plot(column=cols[1], cmap='Blues', figsize=(16, 10), scheme='equal_interval', k=5, legend=True)

df.plot(ax=ax, color='#fafafa', hatch='///')

ax.set_title('sfa', fontdict={'fontsize': 20}, loc='left')
ax.annotate('ddd', xy=(0.1, 0.1), size=12, xycoords='figure fraction')

ax.set_axis_off()
ax.set_xlim([-1.5e7, 1.7e7])
ax.get_legend().set_bbox_to_anchor((.12, .4))
ax.get_figure()
plt.show()
