import numpy as np
import math
import pandas as pd
import seaborn as sns


sns.set_theme()

with open('../data/input_data/МНК.txt') as f:
    data = f.readlines()
    t = []
    p = []
    B = 0.8403
    R = 8.31441

    for i, s in enumerate(data[1:]):
        obj = s.replace('\n', "").split()
        t.append(float(obj[0]))
        p.append(float(obj[1]))
    t = np.array(t) + 273.15
    p = np.array(p) * 133.322
    x = []
    y = []

    for t1, p1 in zip(t, p):
        x.append(-1/t1)
        y.append(math.log10(p1) + B*math.log10(t1))

    x = np.array(x)
    y = np.array(y)

    mtx = np.vstack([x, np.ones(len(x))]).T
    C, A = np.linalg.lstsq(mtx, y, rcond=None)[0]

    res_df = pd.DataFrame(index=pd.Index(list(range(1, 16)), name='i'),
                          columns=['Xi', '1/Xi', 'Yi', 'A*Xi+B', 'Delta'])

    for col, res in zip(res_df.columns, [-1/x, -x, y, C*x + A, y - (C*x + A)]):
        res_df.loc[:, col] = res
    print(f'Уравнение прямой:\n\n'
          f'Y = {-C:.6f} * X + {A:.6f}\n\n\n'
          f'Коэффициент корреляции: r = {np.corrcoef(x, y)[0, 1]:.1f}\n\n'
          f'{"":-^65}\n\n'
          f'{res_df.to_string(col_space=[12 for num in range(len(res_df.columns))], justify="center")}\n\n\n'
          f'DHv = {C*R*math.log(10, math.e):.1f}')

    res_df.to_excel('МНК.xlsx')
