import numpy as np


data = np.load('D:\\Education\\Education\\MFK\\Files\\PCA.npy')
u, s, vh = np.linalg.svd(data)

for num in range(1, len(s)):
    Em = np.sum(s[num:])/np.sum(s)
    if Em < 0.2:
        print(num)
        break
    else:
        pass