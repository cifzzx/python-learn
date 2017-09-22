import os

import numpy as np
from matplotlib import pyplot as pl

path = os.path.dirname(os.path.realpath(__file__)) + '/train_data.txt'
alpha = 0.0001
epsilon = 0.000001


def build_matrix(file_path):
    with open(file_path, 'r') as f:
        data_lines = f.readlines()
        total_lines = len(data_lines)
        train_matrix = np.zeros((total_lines, 2))
        index = 0
        for line in data_lines:
            train_matrix[index, :] = line.split(',')
            index += 1

    return train_matrix


def h_x(theta0, theta1, x):
    return theta0 + theta1 * x


def cost_function(theta0, theta1):
    m = matrix.shape[0]
    cost_sum = 0.
    for data in matrix:
        cost_sum += (h_x(theta0, theta1, data[0]) - data[1]) ** 2

    return cost_sum / (2 * m)


def pd_theta0(theta0, theta1):
    m = matrix.shape[0]
    pd_sum = 0.
    for data in matrix:
        pd_sum += (h_x(theta0, theta1, data[0]) - data[1])

    return pd_sum / m


def pd_theta1(theta0, theta1):
    m = matrix.shape[0]
    pd_sum = 0.
    for data in matrix:
        pd_sum += (h_x(theta0, theta1, data[0]) - data[1]) * data[0]

    return pd_sum / m


def gradient_descent():
    theta0 = 0.
    theta1 = 0.
    cost = cost_function(theta0, theta1)
    print('first time cost: ', cost)
    while True:
        count = 0
        if count > matrix.shape[0]:
            break

        temp_theta0 = theta0 - alpha * pd_theta0(theta0, theta1)
        temp_theta1 = theta1 - alpha * pd_theta1(theta0, theta1)

        theta0 = temp_theta0
        theta1 = temp_theta1

        current_cost = cost_function(theta0, theta1)
        print('current_cost: ', current_cost)

        if abs(current_cost - cost) < epsilon:
            break
        else:
            cost = current_cost
        count += 1

    return theta0, theta1

if __name__ == '__main__':
    matrix = build_matrix(path)
    p0, p1 = gradient_descent()

    X = np.linspace(0, 25, 2, endpoint=True)
    Y = np.ones((len(X), 1))
    i = 0
    for x in X:
        Y[i] = h_x(p0, p1, x)
        i += 1

    pl.plot(X, Y)
    pl.plot(matrix[:, 0], matrix[:, 1], 'o')
    pl.show()

    print('theta0: ', p0, 'theta1: ', p1)
    print('predict: ', h_x(p0, p1, 5.2524))
