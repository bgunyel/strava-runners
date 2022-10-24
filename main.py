import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import gpxpy
import lxml

import gpx_utils
import utils
import stats
import constants


def development():
    # df = utils.read_data()

    #    map_name = 'berlin_marathon'
    map_name = 'Morning_Walk'
    df = gpx_utils.read_gpx_to_df(file_path=constants.DATA_FOLDER + f'{map_name}.gpx')

    distance_types = [constants.GREAT_CIRCLE, constants.GEODESIC,
                      constants.EUCLIDEAN_GREAT_CIRCLE, constants.EUCLIDEAN_GEODESIC]
    for distance_type in distance_types:
        time1 = datetime.datetime.now()
        df[distance_type + '_speed'] = gpx_utils.calculate_speed(df=df, distance_type=distance_type)
        time2 = datetime.datetime.now()
        print(f'{distance_type}: {time2 - time1}')
    gpx_utils.visualize_track_on_map(df=df, map_name=map_name)

    dummy = -32


def main(params):
    print(params['name'])

    development()

    dummy = -32


if __name__ == '__main__':
    parameters = {'name': 'Strava Runners'}

    print('------------------')
    print(f'STARTED EXECUTION @ {datetime.datetime.now()}')
    print('------------------')

    main(params=parameters)

    print('------------------')
    print(f'FINISHED EXECUTION @ {datetime.datetime.now()}')
    print('------------------')
