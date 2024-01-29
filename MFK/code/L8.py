import numpy


def precision(y_true, y_pred):
    """
    TODO: Заполните тело функции вычисления точности предсказания
    """
    true_positive = 0
    false_positive = 0
    for pred, tr in zip(y_pred, y_true):
        if pred == 1 and tr == 1:
            true_positive += 1
        elif pred == 1 and tr != 1:
            false_positive += 1
    prsn = true_positive/(true_positive+false_positive)
    return prsn


def recall(y_true, y_pred):
    """
    TODO: Заполните тело функции вычисления полноты предсказания
    """
    true_positive = 0
    false_negative = 0
    for pred, tr in zip(y_pred, y_true):
        if pred == 1 and tr == 1:
            true_positive += 1
        elif pred == 0 and tr == 1:
            false_negative += 1
    rec = true_positive/(true_positive+false_negative)
    return rec


def f1(y_true, y_pred):
    """
      TODO: Заполните тело функции вычисления f1-меры предсказания
      """

    prsn = precision(y_true, y_pred)
    rec = recall(y_true, y_pred)
    f1_measure = 2*(prsn*rec)/(prsn + rec)
    return f1_measure

