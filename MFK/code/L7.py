import numpy as np


class sample(object):
    def __init__(self, X, n_subspace):
        self.idx_subspace = self.random_subspace(X, n_subspace)

    def __call__(self, X, y):
        idx_obj = self.bootstrap_sample(X)
        X_sampled, y_sampled = self.get_subsample(X, y, self.idx_subspace, idx_obj)
        return X_sampled, y_sampled

    @staticmethod
    def bootstrap_sample(X, random_state=42):
        """
        Заполните тело этой функции таким образом, чтобы она возвращала массив индексов выбранных при помощи бэггинга индексов.
        Пользуйтесь только инструментами, реализованными в numpy.random, выставляя везде, где это необходимо, random_state=42
        """
        res = []
        inds = list(range(len(X)))
        R = np.random.RandomState()
        for obj in range(len(X)):
            res.append(R.choice(inds))
        res = np.unique(res)
        return res

    @staticmethod
    def random_subspace(X, n_subspace, random_state=42):
        """
        Заполните тело этой функции таким образом, чтобы она возвращала массив индексов выбранных при помощи метода случайных подпространств признаков
        Количество этих признаков передается при помощи аргумента n_subspace
        Пользуйтесь только инструментами, реализованными в numpy.random, выставляя везде, где это необходимо, random_state=42
        """
        reslt = []
        R = np.random.RandomState()
        inds = list(range(len(X[0])))
        while len(np.unique(reslt)) != n_subspace:
            reslt.append(R.choice(inds))
        reslt = np.unique(reslt)
        return reslt

    @staticmethod
    def get_subsample(X, y, idx_subspace, idx_obj):
        """
        Заполните тело этой функции таким образом, чтобы она возвращала подвыборку x_sampled, y_sampled
        по значениям индексов признаков(idx_subspace) и объектов(idx_obj) , которые должны в неё попасть
        """
        X_sel = X[idx_obj, :]
        x_sampled = X_sel[:, idx_subspace]
        y_sampled = y[idx_obj]
        return x_sampled, y_sampled


X = np.array([[1,2,3], [4,5,6], [7,8,9]])
Y = np.array([1, 2, 3])
s = sample(X, 2)

bootstrap_indices = s.bootstrap_sample(X)
X_sampled, y_sampled = s.get_subsample(X, Y, s.idx_subspace, bootstrap_indices)
print(X_sampled, y_sampled)
print(bootstrap_indices)
print(s.idx_subspace)
# print(s.idx_subspace)
# print(bootstrap_indices)
# print(X_sampled)
# print(y_sampled)
# res = []
# R = np.random.RandomState(42)
# inds = list(range(len(X.T)))
# for obj in range(8):
#     res.append(R.choice(inds))
# res = np.unique(res)
# print(res)