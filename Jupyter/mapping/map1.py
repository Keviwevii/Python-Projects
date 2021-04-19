# folium helps map with python and converts it to html, css and javascript
# We are reading our txt to a dataframe with pandas

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


# a function to decide color markers
def color_producer(elevation):
    if elevation < 1000:
        return '#007849'
    elif elevation < 3000:
        return '#ffa500'
    else:
        return '#ff0000'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# This feature group puts markers for each volcano
# We use a for loop to go through our data from the txt
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=(lt, ln), popup=str(el) + "m", color=color_producer(el), fill=True,
                                      radius=6))
# Using GeoJson to sort by population in world.json
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {
                                 'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adding our child feature groups
map.add_child(fgv)
map.add_child(fgp)
map.add_child((folium.LayerControl()))

map.save("Map1.html")
