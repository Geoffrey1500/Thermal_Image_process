import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import cv2


def data2array(self):
    data_original = pd.read_csv(self.path, sep='，', header=None, encoding='utf-8', engine='python')
    data_pro = data_original.drop([0, 0])

    item_court = list(data_pro.iloc[0][:])[0]
    item_court = item_court.split(',')
    item_court = [float(item_court[i]) for i in range(1, len(item_court))]
    data_in_array = np.zeros(shape=(1, len(item_court)))

    for line in range(0, len(data_pro)):
        item = list(data_pro.iloc[line][:])[0]
        '''
        The last row of original data is abnormal. The last item in this row should be removed.
        '''
        if line != len(data_pro) - 1:
            item = item.split(',')
            item = [float(item[i]) for i in range(1, len(item))]
        else:
            item = item.split(',')[0:-1]
            item = [float(item[i]) for i in range(1, len(item))]

        item_array = np.array(item).reshape((1, -1))

        data_in_array = np.concatenate([data_in_array, item_array], axis=0)

    data_in_array = np.delete(data_in_array, 0, axis=0)
    resolution_i = data_in_array.shape[0]
    resolution_j = data_in_array.shape[1]
    pixels = resolution_i * resolution_j

    print("The resolution of thermal image is %d x %d" % (resolution_i, resolution_j))
    print("The total pixels is %d" % pixels)

    return data_in_array