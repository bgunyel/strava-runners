import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

import constants


def read_data():
    df = pd.read_csv(filepath_or_buffer=constants.DATA_FILE, sep=';')
    df.rename(columns={constants.GENDER_FR: constants.GENDER,
                       constants.DATE_TIME_FR: constants.DATE_TIME,
                       constants.ELAPSED_TIME_FR: constants.ELAPSED_TIME,
                       constants.ELEVATION_GAIN_FR: constants.ELEVATION_GAIN,
                       constants.AVERAGE_HEART_RATE_FR: constants.AVERAGE_HEART_RATE},
              inplace=True)

    df[constants.DATE_TIME] = pd.to_datetime(df[constants.DATE_TIME], dayfirst=True)
    df[constants.WEEK_DAY] = df[constants.DATE_TIME].dt.weekday + 1
    df[constants.YEAR] = df[constants.DATE_TIME].dt.year
    df[constants.MONTH] = df[constants.DATE_TIME].dt.month
    df[constants.DAY] = df[constants.DATE_TIME].dt.day
    df[constants.HOUR] = df[constants.DATE_TIME].dt.hour
    df[constants.QUARTER] = df[constants.DATE_TIME].dt.quarter

    df[constants.WEEKEND] = False
    df.loc[df[constants.WEEK_DAY].isin([6, 7]), constants.WEEKEND] = True

    df[constants.SLOPE] = df[constants.ELEVATION_GAIN] / df[constants.DISTANCE]
    df[constants.SPEED] = (df[constants.ELAPSED_TIME] / 60) / (df[constants.DISTANCE] / 1000)

    out_df = clean_data(df=df)

    return out_df


def clean_data(df):

    out_df = df.copy(deep=True)

    # Filtering too good results with the help of world records
    distances = np.array(constants.WORLD_RECORD_SPEEDS[constants.DISTANCE])
    men_speed = np.array(constants.WORLD_RECORD_SPEEDS[constants.MEN])
    women_speed = np.array(constants.WORLD_RECORD_SPEEDS[constants.WOMEN])

    x = out_df[constants.DISTANCE].to_numpy()

    interpolation_type = 'linear'
    f_men = interp1d(distances, men_speed, kind=interpolation_type, assume_sorted=True, fill_value='extrapolate')
    f_women = interp1d(distances, women_speed, kind=interpolation_type, assume_sorted=True, fill_value='extrapolate')
    y_men = f_men(x)
    y_women = f_women(x)

    out_df[constants.RECORD] = y_men
    mask = out_df[constants.GENDER] == 'F'
    out_df.loc[mask, constants.RECORD] = y_women[mask]

    # Cleaning
    out_df.drop(out_df[out_df[constants.DISTANCE] < 1000].index, inplace=True)
    out_df.drop(out_df[out_df[constants.SPEED] > 12].index, inplace=True)  # Drop runs with time worse than 12 min/km
    out_df.drop(out_df[out_df[constants.ELAPSED_TIME] < 120].index, inplace=True)
    out_df.drop(out_df[out_df[constants.SPEED] < out_df[constants.RECORD] * 0.90].index, inplace=True)




    return out_df


