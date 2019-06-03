import folium
import sys
import pandas
from pathlib import Path

inFile = 'Volcanoes.txt'
outFile = 'Map.html'
nyc_coords = [40.710377, -73.991997]

def main():
    map = folium.Map(location=[38.58, -99.09], tiles="Mapbox Bright", zoom_start=5)
    data = pandas.read_csv(inFile)
    featureGroup = createFeatureGroup(data)
    map.add_child(featureGroup)
    map.save(outFile);

def createFeatureGroup(data):
    featureGroup = folium.FeatureGroup(name='MyMap')
    lat = list(data["LAT"])
    lon = list(data["LON"])
    names = list(data["NAME"])
    for lt, ln, name in zip(lat,lon,names):
        featureGroup.add_child(folium.Marker(location=[lt,ln], popup=name, icon=folium.Icon(color='green')))
    return featureGroup

if __name__ == '__main__':
    if not Path(inFile).is_file():
        print("File [ %s ] doesn't exist. Exiting..." % inFile)
        sys.exit()
    main()
