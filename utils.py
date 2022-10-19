import pandas as pd

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

    return df

