import os, sys
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

# filename = os.path.join(APP_FOLDER,'data/eq_1_day_m1.json')
filename = os.path.join(APP_FOLDER,'data/eq_data_30_day_m1.json')
with open(filename) as f:
    all_eq_data = json.load(f)
   
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts =[],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes
# data = [Scattergeo(lon=lons,lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color': mags,
        'colorscale':'Reds',
        # 'reversescale': True,
        'colorbar':{'title':'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthqueakes.html')
print(mags[:10])
print(lons[:5])
print(lats[:5])
readable_file = os.path.join(APP_FOLDER,'data/readable_eq_data.json')
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)