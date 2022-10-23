import datetime

import branca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import gpxpy
import lxml
import folium

import utils
import stats
import constants


def read_gpx_to_df(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx_strava = gpxpy.parse(gpx_file)

    points_list = []
    for track in gpx_strava.tracks:
        for segment in track.segments:
            for point in segment.points:
                point_dict = {constants.DATE_TIME: point.time,
                              constants.LATITUDE: point.latitude,
                              constants.LONGITUDE: point.longitude,
                              constants.ELEVATION: point.elevation}
                extension_dict = {lxml.etree.QName(child).localname: float(child.text) for child in point.extensions[0]}

                point_dict = {**point_dict, **extension_dict}

                points_list.append(point_dict)

    df = pd.DataFrame(points_list)
    return df


def visualize_track_on_map(df, map_name):

    tiles = 'OpenStreetMap'

    # df['color'] = df[constants.HR].rolling(2).mean()

    center_lat = (df[constants.LATITUDE].min() + df[constants.LATITUDE].max()) / 2
    center_lon = (df[constants.LONGITUDE].min() + df[constants.LONGITUDE].max()) / 2
    coordinates = [tuple(x) for x in df[[constants.LATITUDE, constants.LONGITUDE]].to_numpy()]

    track_map = folium.Map(location=[center_lat, center_lon], width=1536, height=864, tiles=tiles, zoom_start=13)


    features_list = [constants.HR, constants.CAD]
    colors = ['#0000FF', '#FF00FF', '#FF0000']

    for feature in features_list:
        feature_group = folium.FeatureGroup(feature)
        color_ids = list(df[feature].rolling(2).mean()[1:].to_numpy())
        percentiles = np.percentile(a=color_ids, q=[5, 95])
        color_map = branca.colormap.LinearColormap(vmin=percentiles[0], vmax=percentiles[1], colors=colors)
        folium.ColorLine(positions=coordinates, colors=color_ids, colormap=color_map, weight=4).add_to(feature_group)
        feature_group.add_to(track_map)

    base_feature_group = folium.FeatureGroup('Base')
    folium.PolyLine(coordinates, weight=6).add_to(base_feature_group)
    base_feature_group.add_to(track_map)

    folium.LayerControl(collapsed=False).add_to(track_map)
    track_map.save(f'{constants.OUT_FOLDER}{map_name}.html')

    dummy = -32

