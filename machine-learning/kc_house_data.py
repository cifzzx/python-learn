import os

import numpy as np


def compute_feature(org_data_set):
    years_of_house_list = []
    for row in org_data_set:
        print(type(row[1]), ' ', row[1], ' ', row[14])
        years_of_house = int(row[1][0:4]) - row[14]
        years_of_house_list.append(years_of_house)

    age_of_house = np.asarray([years_of_house_list], dtype=float)
    org_data_set = np.concatenate((org_data_set, age_of_house.T), axis=1)
    return np.delete(org_data_set, np.s_[0, 1, 14], 1)


def feature_normalization(fea_data):
    data_avg = np.sum(fea_data, dtype=float) / (fea_data.shape[0])
    data_sta = np.std(fea_data, dtype=float)
    return (fea_data - data_avg) / data_sta


def h_x(matrix_x, theta):
    return theta.T.dot(matrix_x)


def gradient_descent(matrix_x, matrix_y, theta, alpha, iter):
    m = matrix_y.size
    cost = np.zeros((iter, 1))
    for i in range(iter):
        print('the ', i, 'times iterator')
        hx = np.dot(matrix_x, theta.T)  # matrix_x: n * m, theta: 1 * m, hx: n * 1
        theta = theta - alpha * (matrix_x.T.dot((hx - matrix_y)) / m)
        cost[i] = cost_function(X, y, theta)
        print(i, ' theta: ', theta, '\n')
        print(i, ' cost: ', cost)

    return theta, cost


def cost_function(matrix_x, matrix_y, theta):
    return np.sum((np.dot(matrix_x, theta.T) - matrix_y) ** 2) / (2 * matrix_y.size)


if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__)) + '/kc_house_data.npz'
    data = np.load(file=path, mmap_mode='r')
    train_data_org = data['train']
    test_data_org = data['test']

    train_data = compute_feature(train_data_org)
    test_data = compute_feature(test_data_org)

    # feature Normalization
    new_train_data = feature_normalization(train_data)
    ones = np.ones((new_train_data.shape[0], 1), dtype=float)

    X = np.delete(new_train_data, np.s_[0], 1)  # remove column one, get X
    X = np.concatenate([ones, X], axis=1)
    y = np.delete(new_train_data, np.s_[1:], 1)  # remove column expect no.1, get y
    Theta = np.random.rand(1, X.shape[1])  # generate theta [0-1)

    alpha = 0.1  # learning rate
    iter_count = 300

    j_theta, cost = gradient_descent(X, y, Theta, alpha, iter_count)

    print('j_theta: ', j_theta, '\n')
    print('cost: ', cost)
