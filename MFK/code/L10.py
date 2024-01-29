from sklearn.cluster import KMeans
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
files_ls = [file for file in os.listdir('D:\\Education\\Education\\MFK\\Files') if file[-3:] == 'csv'][:-1]
n_clusters = [2, 4, 3, 3, 4, 3]
print(files_ls)
for f, n in zip(files_ls, n_clusters):
    data = pd.read_csv(f'D:\\Education\\Education\\MFK\\Files\\{f}')
    if len(data.columns) == 4:
        data = data.drop(data.columns[0], axis=1)
    data.columns = ['a0', 'a1', 'class']

    # sns.scatterplot(data=data, x='a0', y='a1', hue='class')
    # plt.show()
    # plt.close()
    X = data.iloc[:, [0, 1]].to_numpy()
    y = data.iloc[:, 2].to_numpy()
    colors_clusters = ['g', 'b', 'r', '#ff8243']
    print(X)
    kmeans = KMeans(n_clusters=n, random_state=42).fit(X)
    plt.figure(figsize=(10, 10))
    for i, p in enumerate(X):
        plt.scatter([p[0]], [p[1]], c=colors_clusters[kmeans.labels_[i]])
    plt.show()
    plt.close()

# X = [[p.x, p.y] for p in points]
