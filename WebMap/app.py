# Import section
import folium
import sys
import pandas
from pathlib import Path

# File variables
geoFile = 'world.json'
volcanoFile = 'Volcanoes.txt'
outFile = 'Map.html'

# HTML template for marker popups
html = """
<h4>Volcano Information</h4>
Name: %s
<br>
Elevation: %s m
"""

# Determine which color to use
# Parameters:
#   elev -> int : elevation of volcano
def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif elev < 3000:
        return 'orange'
    return 'red'

# Create a folium marker
# Parameters:
#   lt -> int : latitude position
#   ln -> int : longitude position
#   iframe -> folium.IFrame : created html iframe with text to place at this CircleMarker
#   color -> string : fill_color of the marker
def createMarker(lt,ln, iframe, color):
    return folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe),
                               radius=6, color='grey', fill_color=color, fill_opacity=0.7)

# Create volcano Feature Group
# Parameters:
#   map -> folium.Map : The map to add the feature group to
def addVolcanoFeatureGroup(map):
    featureGroup = folium.FeatureGroup(name='Volcanoes')
    addVolcanoInformation(featureGroup)
    map.add_child(featureGroup)

# Create volcano information
# Parameters:
#   featureGroup -> folium.FeatureGroup : The feature group to add to
def addVolcanoInformation(featureGroup):
    data = pandas.read_csv(volcanoFile)
    lat = list(data["LAT"])
    lon = list(data["LON"])
    names = list(data["NAME"])
    elev = list(data["ELEV"])
    for lt, ln, name, el in zip(lat,lon,names,elev):
        iframe = folium.IFrame(html=html % (name, str(el)), width=200, height=100)
        featureGroup.add_child(createMarker(lt,ln, iframe, color_producer(el)))

# Create geo data feature group
# Parameters:
#   map -> folium.Map : The map to add the feature group to
def addGeoDataFeatureGroup(map):
    featureGroup = folium.FeatureGroup(name='Population')
    addGeoData(featureGroup)
    map.add_child(featureGroup)

# Add geo data to the feature group
# Parameters:
#   featureGroup -> folium.FeatureGroup : The feature group to add the geo data to
def addGeoData(featureGroup):
    file = open(geoFile, 'r', encoding='utf-8-sig').read()
    featureGroup.add_child(folium.GeoJson(data=file,
                                          style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                                                        else 'orange' if x['properties']['POP2005'] < 20000000
                                                                                        else 'red'}))
# Add layer control to the map
# Parameters:
#   map -> folium.Map : The map to add the layer control to
def addLayerControl(map):
    map.add_child(folium.LayerControl())

# Main function - Create the map and add features
def main():
    map = folium.Map(location=[38.58, -99.09], tiles="Mapbox Bright", zoom_start=5)
    addVolcanoFeatureGroup(map)
    addGeoDataFeatureGroup(map)
    addLayerControl(map)
    map.save(outFile)

if __name__ == '__main__':
    # Make sure files exist before trying to start program
    if not Path(volcanoFile).is_file():
        print("File [ %s ] doesn't exist. Exiting..." % volcanoFile)
        sys.exit()
    elif not Path(geoFile).is_file():
        print("File [ %s ] doesn't exist. Exiting..." % geoFile)
        sys.exit()
    main()
