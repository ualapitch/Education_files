import pandas as pd
import numpy as np
import math


def euler_method(point=None, interval=None, step=None, func=None):
    x = np.arange(interval[0], interval[1]+step, step)
    y = [point[1]]
    for val_x in x[:-1]:
        val_y = y[-1]
        f = func(val_x, val_y)
        y_new = val_y + step*f
        y.append(y_new)

    return x, y


x, y = euler_method([0, 0], [0, 1], 0.1, lambda x, y: y + x)
y_true = [round(math.exp(s) - s - 1, 4) for s in x]
res_df = pd.DataFrame()
res_df.loc[:, 'x '] = [round(num, 4) for num in x]
res_df.loc[:, 'м-д Эйлера'] = [round(num, 4) for num in y]
res_df.loc[:, 'Точное значение'] = y_true
res_df.loc[:, 'Погрешность'] = [round(val1 - val2, 4) for val1, val2 in zip(y_true, y)]
print(f'Начальное условие: x0 = 0, y0 = 0\n\n'
      f'x_кон. = 1         шаг по x: 0.1\n\n'
      f'{res_df.to_string(col_space=[12 for num in range(len(res_df.columns))], justify="center", index=False)}')

