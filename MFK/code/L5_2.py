from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import os


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


files = os.listdir('D:\\Education\\Education\\MFK\\Files')
res = []
for f in files[:-1]:
    data = np.load(f'D:\\Education\\Education\\MFK\\Files\\{f}')
    X = data[:, 0].reshape(-1, 1)
    y = data[:, 1].reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    res.append((f, r2(y_test, preds)))

print(res)

