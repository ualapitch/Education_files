import seaborn as sns
import pandas as pd
import urllib as url
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mtx = pd.read_csv('/MFK/Files/data_for_task.csv')
print(mtx)


X = mtx.iloc[:, :-1].to_numpy()
y = mtx.iloc[:, -1].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# Now lets train svm model
model = svm.SVC(random_state=241, kernel='linear')
model.fit(X_train, y_train)

# Lets predict for new input
preds = model.predict(X_test)
print(accuracy_score(y_test, preds))

