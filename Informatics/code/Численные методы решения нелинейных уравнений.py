import math


def dichotomy_method(f, a, b, epsilon=10E-6):
    if f(a) * f(b) > 0:
        return None

    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def func(x, p=0.4):
    # 4x + 2 = (1-x) + (1-x) + 4x
    pch4 = p*(1-x)/(2*x+2)
    pnh3 = p*(1-x)/(2*x+2)
    phcn = p*x/(2*x+2)
    ph2 = 3*p*x/(2*x+2)
    fnc = (phcn*ph2**3)/(pch4*pnh3) - 10**-2.361
    return fnc


conc = dichotomy_method(func, 0, 0.999999)
print(f'При давлении 0,4 атм и lg Kp = -2.361\n'
      f'Было получено {round(conc/(2+2*conc)*100, 2)} % HCN')
