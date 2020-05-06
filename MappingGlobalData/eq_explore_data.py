import os, sys
import json

from plotly.graph_obs import Scattergeo, Layout
from plotly import offline

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

filename = os.path.join(APP_FOLDER,'data/eq_1_day_m1.json')
with open(filename) as f:
    all_eq_data = json.load(f)
   
all_eq_dicts = all_eq_data['features']

mags, lons, lats =[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
readable_file = os.path.join(APP_FOLDER,'data/readable_eq_data.json')
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)