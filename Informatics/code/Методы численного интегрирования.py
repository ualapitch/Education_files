import numpy as np
import math
import pandas as pd
from decimal import Decimal


def integrate(a: int or float, b: int or float, func, antideriviate_func, method=None, num_subsegments=None):
    if method is None:
        method = 'left_square'
    if num_subsegments is None:
        num_subsegments = 50
    subsegments = np.linspace(a, b, num_subsegments + 1)
    sub_length = subsegments[1]-subsegments[0]
    area = 0
    newton_leibniz = antideriviate_func(b) - antideriviate_func(a)

    if method == 'left_square':
        for x in subsegments[:-1]:
            area += func(x)
        return area*sub_length,  f'{Decimal(newton_leibniz - area*sub_length):.5E}'
    elif method == 'right_square':
        for x in subsegments[1:]:
            area += func(x)
        return area*sub_length,  f'{Decimal(newton_leibniz - area*sub_length):.5E}'
    elif method == 'trapezoid':
        for x in subsegments[:-1]:
            area += (func(x+sub_length) + func(x))/2
        return area*sub_length,  f'{Decimal(newton_leibniz - area*sub_length):.5E}'
    elif method == 'parabola':
        if num_subsegments % 2 == 0:
            for i, x in enumerate(subsegments):
                if i == 0 or i == num_subsegments:
                    area += func(x)
                elif i % 2 != 0:
                    area += 4*func(x)
                elif i % 2 == 0:
                    area += 2 * func(x)
            return area*sub_length/3,  f'{Decimal(newton_leibniz - area*sub_length/3):.5E}'


subsegments = 100
res_df = pd.DataFrame(columns=['Интеграл', 'Ошибка вычислений'],
                      index=pd.Index(['Прямоуг. лев.', 'Прямоуг. прав.', 'Трапеций', 'Парабол'], name='Метод'))
for row, method in zip(res_df.index, ['left_square', 'right_square', 'trapezoid', 'parabola']):
    res_df.loc[row] = integrate(0.5, 1.5, lambda x: 1/x, lambda x: math.log(x), method, subsegments)

print('Число элементарных отрезков\n'
      f'{subsegments}\n\n'
      f'{res_df.to_string(col_space=[15 for num in range(len(res_df.columns))], justify="center")}')
