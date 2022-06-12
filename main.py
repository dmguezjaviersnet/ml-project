import warnings

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from sklearn import metrics  # for evaluations
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import (  # for generating experimental data
    make_blobs,
    make_circles,
)
from sklearn.preprocessing import StandardScaler  # for feature scaling

from tools import get_data


def main():
    accel_data = get_data("accelerometer", "./data/bumps.json")
    gyro_data = get_data("gyroscope", "./data/bumps.json")

    accel_x, accel_y, accel_z = accel_data[0], accel_data[1], accel_data[2]
    gyro_x, gyro_y, gyro_z = gyro_data[0], gyro_data[1], gyro_data[2]

    # print(accel_x)
    # print(accel_y)
    # print(accel_z)
    # print(accel_x)
    # print(accel_y)
    # print(accel_z)


if __name__ == "__main__":
    main()
