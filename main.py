import datetime

import utils


def development():
    df = utils.read_data()

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
