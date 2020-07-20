import gmaps
import gmaps.datasets
import gmaps.geojson_geometries

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# Census & gmaps API Keys
from config import census_key, g_key

# Configure gmaps
gmaps.configure(api_key=g_key)

countries_geojson = gmaps.geojson_geometries.load_geometry('countries')

fig = gmaps.figure()
