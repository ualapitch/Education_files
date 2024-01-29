import numpy as np


def r2(y_true, y_pred):
    De = 0
    Dz = 0
    for y_tr in y_true:
        Dz += (y_tr - np.mean(y_true))**2
    Dz *= 1/len(y_true)
    for y_tr, y_pr in zip(y_true, y_pred):
        De += (y_tr - y_pr)**2
    De *= 1/len(y_true)
    return 1 - De/Dz