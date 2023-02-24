# f(x) = -12*x**4*sin(cos(x)) - 18x**3+5x**2 + 10*x - 30
#Определить корни
#Найти интервалы, на которых функция возрастает
#Найти интервалы, на которых функция убывает
#Построить график
#Вычислить вершину
#Определить промежутки, на котором f > 0
#Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

limit = 100
step = 0.01
color = 'b'
line_stile = '-'
direct_up = True

a, b, c, d, e = -12, -18, 5, 10, -30

x = np.arange(-limit, limit, step)

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def switch_line():
    global line_stile
    if line_stile == '-':
        line_stile = '--'
    else:
        line_stile = '-'
    return line_stile


def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

x_change = [(-limit, 'limit')]
for i in range(len(x) - 1):
    if (func(x[i]) > 0 and func(x[i+1]) < 0) or (func(x[i]) < 0 and func(x[i+1]) > 0):
        x_change.append((x[i], 'zero'))
    if direct_up:
        if func(x[i]) > func((x[i+1], 'direct')):
            x_change.append(x[i])
            direct_up = False
    else:
        if func(x[i]) < func(x[i+1]):
            x_change.append((x[i], 'direct'))
            direct_up = True
x_change.append((limit, 'limit'))

for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i+1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color.lab)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label = 'Убывание > 0')
plt.plot(0, 0, 'r', label = 'Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label = 'Убывание < 0')
plt.plot(0, 0, 'r', label = 'Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')


plt.grid()
plt.show()