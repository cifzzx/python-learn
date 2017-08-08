import codecs
import os
import json
company_txt = os.path.dirname(os.path.realpath(__file__)) + '/company.txt'
company_json = os.path.dirname(os.path.realpath(__file__)) + '/company.json'
l = []
d = {}


def txt_to_json():
    file = open(company_txt, 'r')
    while True:
        line = file.readline()
        if line == '':
            break
        l.append(line)
    d['companyList'] = l
    file.close()

    write_to_json(d)


def write_to_json(d):
    with codecs.open(company_json, 'w', 'UTF-8') as output_file:
        json.dump(d, output_file)


if __name__ == '__main__':
    txt_to_json()
