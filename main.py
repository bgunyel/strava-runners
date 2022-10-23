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

    df = gpx_utils.read_gpx_to_df(file_path=constants.DATA_FOLDER + 'Morning_Walk.gpx')

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
