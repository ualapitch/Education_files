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


k1 = 5*10**-2
k2 = 6.5*10**-3
x, y = euler_method([0, 0], [0, 500], 10, lambda t, P: k1*1*math.exp(-k1*t) - k2*P)
res_df = pd.DataFrame()

res_df.loc[:, 't'] = [round(num, 4) for num in x]
res_df.loc[:, '[P]'] = [round(num, 6) for num in y]
res_df.to_excel('Метод Эйлера_11.xlsx')
print(f'Расчет методом Эйлера кинетики хим. реакции\n\n'
      f'Начальное значение t: 0\n'
      f'Начальное значение P: 0\n'
      f'Начальное значение t: 500\n'
      f'Шаг интегрирования: 10\n\n'
      f'{res_df.to_string(col_space=[12 for num in range(len(res_df.columns))], justify="center", index=False)}')