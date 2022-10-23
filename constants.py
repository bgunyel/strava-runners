from typing import Final

DATA_FOLDER: Final = './data/'
OUT_FOLDER: Final = './out/'

FRENCH_DATA_FILE: Final = 'raw-data.csv'
DATA_FILE: Final = DATA_FOLDER + FRENCH_DATA_FILE

WANDB_PROJECT_NAME: Final = 'todo-todo'
WANDB_USER_NAME: Final = 'bertan-gunyel'
WANDB_DYNAMIC_VIS: Final = 'dynamic-vis'
WANDB_STATIC_VIS: Final = 'static-vis'

WANDB_TODO_TODO_TABLE: Final = 'todo-todo-table'

ATHLETE: Final = 'athlete'
GENDER: Final = 'gender'
GENDER_FR: Final = 'genre'
DATE_TIME: Final = 'date_time'
DATE_TIME_FR: Final = 'horodatage'
DISTANCE: Final = 'distance (m)'
ELAPSED_TIME_FR: Final = 'temps (s)'
ELAPSED_TIME: Final = 'elapsed_time (s)'
ELEVATION_GAIN_FR: Final = 'D+ (m)'
ELEVATION_GAIN: Final = 'elevation_gain (m)'
AVERAGE_HEART_RATE_FR: Final = 'FC moyenne (bpm)'
AVERAGE_HEART_RATE: Final = 'average_heart_rate (bpm)'
SLOPE: Final = 'slope'
SPEED: Final = 'speed (min/km)'  # raw speed
ADJUSTED_SPEED: Final = 'adjusted_speed'

LATITUDE: Final = 'latitude'
LONGITUDE: Final = 'longitude'
ELEVATION: Final = 'elevation'
HR: Final = 'hr'  # heart rate
CAD: Final = 'cad'  # cadence

DATE: Final = 'date'
TIME: Final = 'time'
YEAR: Final = 'year'
MONTH: Final = 'month'
DAY: Final = 'day'  # day in the month
WEEK_DAY: Final = 'week_day'
WEEKEND: Final = 'weekend'
HOUR: Final = 'hour'
QUARTER: Final = 'quarter'

MONDAY: Final = 'Monday'
TUESDAY: Final = 'Tuesday'
WEDNESDAY: Final = 'Wednesday'
THURSDAY: Final = 'Thursday'
FRIDAY: Final = 'Friday'
SATURDAY: Final = 'Saturday'
SUNDAY: Final = 'Sunday'

MEN: Final = 'men'
WOMEN: Final = 'women'
RECORD: Final = 'record'

WORLD_RECORD_SPEEDS: Final = {DISTANCE: [1000, 1500, 1609.344, 2000, 3218.688, 5000, 10000, 21097.5, 42195],
                              MEN:      [2.20, 2.29, 2.31,     2.38, 2.48,     2.52, 2.62,  2.73,    2.87],
                              WOMEN:    [2.48, 2.56, 2.61,     2.71, 2.79,     2.82, 2.93,  2.98,    3.18]}

