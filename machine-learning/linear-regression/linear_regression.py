import os

file_path = os.path.dirname(os.path.realpath(__file__)) + '/train_data.txt'
x_list = []
y_list = []


def build_data_list(path):
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break

            x_list.append(line.split(',')[0])
            y_list.append(line.split(',')[1])

    return x_list, y_list


if __name__ == '__main__':
    x_list, y_list = build_data_list(file_path)
    print('x: ', x_list, 'y: ', y_list)
