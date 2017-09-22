import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__)) + '/train_data2.txt'
x1_list = []
x2_list = []
y_list = []
alpha = 0.0001
epsilon = 0.00001


# build matrix x , y
def build_data_list(file_path):
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break

            x1_list.append(float(line.split(',')[0]))
            x2_list.append(float(line.split(',')[1]))
            y_list.append(float(line.split(',')[2]))

    s_x1 = max(x1_list) - min(x1_list)  # x1 standard deviation
    s_x2 = max(x2_list) - min(x2_list)  # x2 standard deviation
    avg_x1 = sum(x1_list) / len(x1_list)  # avg for x1
    avg_x2 = sum(x2_list) / len(x2_list)  # avg for x2

    for i in range(len(x1_list)):
        x1_list[i] = (x1_list[i] - avg_x1) / s_x1

    for j in range(len(x2_list)):
        x2_list[j] = (x2_list[j] - avg_x2) / s_x2

    return x1_list, x2_list, y_list


def build_matrix():
    list1, list2, list3 = build_data_list(path)
    m = len(list1)
    x_list = []
    y_list = []
    for i in range(m):
        l1 = []
        l2 = []
        l1.append(float(1))
        l1.append(list1[i])
        l1.append(list2[i])
        x_list.append(l1)

        l2.append(list3[i])
        y_list.append(l2)

    X = np.array(x_list)
    Y = np.array(y_list)

    print(type(X), ' ', X.shape, '\n', type(Y), ' ', Y.shape)
    print('\n', X, '\n', Y)

    return X, Y


