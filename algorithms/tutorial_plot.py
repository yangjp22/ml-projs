#!/usr/bin/env python
# coding: utf-8


from matplotlib import pyplot as plt
from matplotlib import font_manager



my_font = font_manager.FontProperties(fname = 'C:/Windows/Fonts/SimHei.ttf')
x_3 = list(range(1, 32))
x_10 = list(range(51, 82))
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,16]

fig = plt.figure(figsize = (28, 8), dpi = 80)
plt.scatter(x_3, y_3, label = '3月份')
plt.scatter(x_10, y_10, label = '10月份')

x_ = x_3 + x_10
x_labels = ['3月{}号'.format(i)  for i in x_3]
x_labels += ['3月{}号'.format(i - 50)  for i in x_3]
plt.xticks(ticks = x_[::3], labels=x_labels[::3],fontproperties = my_font, rotation = 45)

plt.xlabel('时间', fontproperties = my_font)
plt.ylabel('气温', fontproperties = my_font)


plt.legend(loc = 'best', prop = my_font)



a = ['猩球崛起:终极之战','敦刻尔克','蜘蛛侠:英雄归来','战狼2']
b_16 = [15476, 312,4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [bar_width + i for i in x_14]
x_16 = [2 * bar_width + i for i in x_14]

plt.figure(figsize = (20, 8), dpi = 80)

plt.bar(x_14, b_14, width = bar_width, label = '9月14日')
plt.bar(x_15, b_15, width = bar_width, label = '9月15日')
plt.bar(x_16, b_16, width = bar_width, label = '9月16日')

plt.xticks(x_15, a,fontproperties = my_font)

plt.legend(loc = 'best', prop = my_font)



a = ['猩球崛起:终极之战','敦刻尔克','蜘蛛侠:英雄归来','战狼2']
b_16 = [15476, 312,4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_height = 0.2

y_14 = list(range(len(a)))
y_15 = [bar_height + i for i in y_14]
y_16 = [2 * bar_height + i for i in y_14]

plt.figure(figsize = (20, 8), dpi = 80)

plt.barh(y_14, b_14, height = bar_height, label = '9月14日')
plt.barh(y_15, b_15, height = bar_height, label = '9月15日')
plt.barh(y_16, b_16, height = bar_height, label = '9月16日')

plt.yticks(y_15, a, fontproperties = my_font)

plt.legend(loc = 'best', prop = my_font)




interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 57]




plt.figure(figsize = (20, 8), dpi = 80)
plt.bar(range(len(quantity)), quantity, width = 1)
x_ = [i - 0.5 for i in range(len(quantity) + 1)]
x_labels = interval + [150]
plt.xticks(x_, x_labels)
plt.grid()


def fill_array(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:,i]
        non_nan_numbers = np.count_nonzero(temp_col != temp_col)
        if non_nan_numbers != 0:
            temp_col_non_nan = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = temp_col_non_nan.mean()
    return t1

