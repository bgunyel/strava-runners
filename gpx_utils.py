import datetime
import itertools

import branca
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import gpxpy
import lxml
import folium

from geopy.distance import great_circle
from geopy.distance import geodesic

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


def calculate_distance(df, distance_type):
    coordinates = [tuple(x) for x in df[[constants.LATITUDE, constants.LONGITUDE]].to_numpy()]
    distances = [np.nan] * len(coordinates)

    if distance_type in [constants.GREAT_CIRCLE, constants.EUCLIDEAN_GREAT_CIRCLE]:
        distances[1:] = [great_circle(coordinates[i], coordinates[i - 1]).m for i in range(1, len(coordinates))]
    elif distance_type in [constants.GEODESIC, constants.EUCLIDEAN_GEODESIC]:
        distances[1:] = [geodesic(coordinates[i], coordinates[i - 1]).m for i in range(1, len(coordinates))]
    else:
        raise Exception('Unsupported Distance Type!')

    if distance_type in [constants.EUCLIDEAN_GREAT_CIRCLE, constants.EUCLIDEAN_GEODESIC]:
        dummy = -32
        elev_diff = df[constants.ELEVATION].diff().abs().to_list()
        distances[1:] = [np.sqrt(elev_diff[i] ** 2 + distances[i] ** 2) for i in range(1, len(coordinates))]

    return distances


def calculate_speed(df, distance_type, step_size=10):
    distances = calculate_distance(df=df, distance_type=distance_type)
    distances[0] = 0
    cum_distances = list(itertools.accumulate(distances))

    step = max(step_size, next(i for i,v in enumerate(cum_distances) if v > 0))

    time_diff = df[constants.DATE_TIME].diff(periods=step).to_list()

    speed_vector = [np.nan] * len(distances)

    speed_vector[step:] = \
        [(time_diff[i].total_seconds() * 1000 / 60) / (cum_distances[i] - cum_distances[i - step]) \
         for i in range(step, len(distances))]

    return speed_vector


def visualize_track_on_map(df, map_name):
    tiles = 'OpenStreetMap'

    # df['color'] = df[constants.HR].rolling(2).mean()

    center_lat = (df[constants.LATITUDE].min() + df[constants.LATITUDE].max()) / 2
    center_lon = (df[constants.LONGITUDE].min() + df[constants.LONGITUDE].max()) / 2
    coordinates = [tuple(x) for x in df[[constants.LATITUDE, constants.LONGITUDE]].to_numpy()]

    track_map = folium.Map(location=[center_lat, center_lon], width=1536, height=864, tiles=tiles, zoom_start=13)

    features_list = [constants.HR, constants.CAD]
    # colors = ['#0000FF', '#FF00FF', '#FF0000']
    colors = ['#0000FF', '#4169E1', '#8A2BE2', '#4B0082', '#483D8B', '#6A5ACD', '#7B68EE', '#9370DB', '#9400D3',
              '#9932CC', '#BA55D3', '#800080', '#C71585', '#FF00FF', '#FF1493', '#F08080', '#FA8072', '#FF6347',
              '#FF4500', '#FF0000']

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
