import numpy as np
import math
import pandas as pd


step = 0.1
A = np.arange(1, 2+step, step)
B = np.linspace(2, 2.5, 6)
res_df = pd.DataFrame(columns=[f'{b:.1f}' for b in B])

for a in A:
    values_ls = []
    for b in B:
        num_prev = 0
        i = 1
        num_cur = (a**2*(math.sin(b) + math.cos(b))) / (b**2*(i**5-math.sin(i)**2))
        while abs(num_cur - num_prev) > 10**(-3):
            i += 1
            num_prev = num_cur
            num_cur += (a ** 2 * (math.sin(b) + math.cos(b))) / (b ** 2 * (i ** 5 - math.sin(i) ** 2))
        values_ls.append(num_cur)
    res_df.loc[a] = values_ls

print('Значение А меняется от 1 до 2 с шагом 0,1\n'
      'Значение В меняется от 2 до 2,5 с шагом 0,1\n\n'
      f'{res_df.to_string(col_space=[15 for num in range(len(res_df.columns))], justify="center")}')


