import folium
import sys
from pathlib import Path

fileName = 'Volcanoes.txt'
nyc_coords = [40.710377, -73.991997]

def main():
    map = folium.Map(location=nyc_coords, tiles="Mapbox Bright")
    featureGroup = createFeatureGroup()
    map.add_child(featureGroup)
    map.save("map_nyc.html");

def createFeatureGroup():
    featureGroup = folium.FeatureGroup(name='MyMap')
    featureGroup.add_child(folium.Marker(location=nyc_coords, popup="Marker Location", icon=folium.Icon(color='green')))
    return featureGroup

if __name__ == '__main__':
    if not Path(fileName).is_file():
        print("file doesn't exist... exiting")
        sys.exit()
    main()
