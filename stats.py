import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

import constants
import utils


def examine_world_records():

    distances = np.array(constants.WORLD_RECORD_SPEEDS[constants.DISTANCE])
    men_speed = np.array(constants.WORLD_RECORD_SPEEDS[constants.MEN])
    women_speed = np.array(constants.WORLD_RECORD_SPEEDS[constants.WOMEN])

    # interpolation_types = ['linear', 'slinear', 'quadratic', 'cubic']
    interpolation_types = ['linear', 'quadratic']

    x = np.arange(start=1050, stop=42200, step=100)

    plt.figure(figsize=(18, 8))
    for kind in interpolation_types:
        f_men = interp1d(distances, men_speed, kind=kind, assume_sorted=True)
        f_women = interp1d(distances, women_speed, kind=kind, assume_sorted=True)
        y_men = f_men(x)
        y_women = f_women(x)
        plt.plot(x, y_men, '-', label=f'Men {kind}')
        plt.plot(x, y_women, '-', label=f'Women {kind}')

    plt.plot(distances, men_speed, 'o')
    plt.plot(distances, women_speed, 'o')
    plt.grid(visible=True)
    plt.legend()
    plt.xlabel('Distance (m)')
    plt.ylabel('Average Speed (min/km)')
    plt.title(f'World Records & Interpolations')
    plt.show()

    dummy = -32
