import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import gpxpy
import lxml

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
