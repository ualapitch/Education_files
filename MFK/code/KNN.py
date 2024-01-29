import numpy as np


class KNN_classifier:
    def __init__(self, n_neighbors: int, **kwargs):
        self.mtx = None
        self.K = n_neighbors

    def fit(self, x: np.array, y: np.array):
        self.mtx = list(zip(x, y))



        # TODO: напишите метод .fit() класса KNN_classifier
        # Эта функция принимает на вход два массива:
        # - x (набор признаков, массив размерности n x m, n - число объектов, m - размерность признакового описания)
        # - y (метки для обучения, одномерный массив размерности n)
        # Эта функция ничего не возвращает, она должна настроить внутренние параметры модели для дальнейшего использования
        # Подумайте, в чем заключается процесс обучения именно этого алгоритма?
        # Что этот алгоритм делает в тот момент, когда он получил обучающую выборку?
        # Реализуйте эту логику в коде
        pass

    def predict(self, x: np.array):

        predictions = []
        for obj in x:
            b_pr = []
            for tr_obj in self.mtx:
                dist = np.linalg.norm(obj - tr_obj[0])
                b_pr.append((dist, tr_obj[1]))
            b_pr_sorted_k = sorted(b_pr)[:self.K]
            pred = np.unique([a[1] for a in b_pr_sorted_k], return_counts=True)
            predictions.append(pred[0][pred[1].argmax()])

        # TODO: напишите метод .predict(x) класса KNN_classifier
        # Этот метод принимает на вход один массив x. Массив x - это двумерный массив объектов, для которых требуется получить предсказание
        # На выходе этой функции мы хотим получить одномерный массив predictions, размерности x.shape[0] (то есть для каждогго объекта массива x мы сделали своё предсказание)
        # Вспомните, как алгоритм KNN делает предсказание?
        # Реализуйте эту логику в коде
        predictions = np.array(predictions)
        return predictions
