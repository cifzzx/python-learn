import os
import numpy as np
from matplotlib import pyplot as pl

path = os.path.dirname(os.path.realpath(__file__)) + '/train_data.txt'
alpha = 0.0001
epsilon = 0.000001
x_list = []
y_list = []


def build_data_list(file_path):
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            x_list.append(float(line.split(',')[0]))
            y_list.append(float(line.split(',')[1]))

    return x_list, y_list


def h_x(theta, x):
    return theta * x


def cost_function(theta):
    m = len(x_list)
    cost_sum = 0.

    for index in range(m):

        cost_sum += (h_x(theta, x_list[index]) - y_list[index]) ** 2

    return cost_sum / (2 * m)


def pd_theta(theta):
    m = len(x_list)
    gd_sum = 0.

    for index in range(m):
        gd_sum += (h_x(theta, x_list[index]) - y_list[index]) * x_list[i]

    return gd_sum / m


def gradient_descent():
    theta = 0.
    cost = cost_function(theta)
    count = 0
    while True:
        if count > len(x_list):
            break

        theta -= alpha * pd_theta(theta)

        current_cost = cost_function(theta)

        if abs(current_cost - cost) < epsilon:
            break
        else:
            cost = current_cost
        count += 1
    return theta


if __name__ == '__main__':
    x_list, y_list = build_data_list(path)
    p1 = gradient_descent()

    X = np.linspace(0, 25, 2, endpoint=False)
    Y = np.ones((len(X), 1))
    i = 0
    for x in X:
        Y[i] = h_x(p1, x)
        i += 1

    pl.plot(X, Y)
    pl.plot(x_list, y_list, 'o')
    pl.show()

    print(p1 * 5.4369)
