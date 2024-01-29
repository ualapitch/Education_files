import numpy as np
import math


def func(s: float, r: float):
    fnc = math.exp(-0.0076*s**2)*math.sin(2.67*s - 0.00004*s**3)/s
    fin_func = fnc*(math.sin(s*r)/(s*r))
    return fin_func


a = 0.0000001
b = 30
num_subsegments = 150
subsegments = np.linspace(a, b, num_subsegments + 1)
sub_length = subsegments[1]-subsegments[0]
print(f'Шаг интегрирования по s:  {round(sub_length, 2)}\n')
print(f'{"r": ^12}{"P(r)": ^12}\n'
      f'{"":-^22}')
for r in np.arange(2.2, 3.05, 0.05):
    area = sub_length*((func(subsegments[0], r) + func(subsegments[-1], r))/2 + sum([func(s, r) for s in subsegments[1:-1]]))
    print(f'{round(r, 2): ^12}{round(area, 5): ^12}')
