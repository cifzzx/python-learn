# coding = utf-8
import codecs
import json
import os
import random
import string
from json import load
from time import gmtime, strftime

company_json = os.path.dirname(os.path.realpath(__file__)) + '/company.json'
company_txt = os.path.dirname(os.path.realpath(__file__)) + '/company.txt'

code_level = 1
has_child = 0
parent_id = ' '
short_name = ' '
spelling = ' '
org_level = 1
status = 0
date_to = ' '
creator = 0
who_modified = 0
remark = ' '
row_id = 'AAAWziAAFAAAAFUAAA'
status_time = strftime('%Y-%m-%d %H:%M', gmtime())
date_from = strftime('%Y-%m-%d', gmtime())
time_created = strftime('%Y-%m-%d %H:%M', gmtime())
time_modified = strftime('%Y-%m-%d %H:%M', gmtime())


def id_generator(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def build_insert_sql():
    code_id = 1
    sequence = 1
    company_dic = load(codecs.open(company_json, "r", "UTF-8"))
    l = []
    for company in company_dic['companyList']:
        tree_code = '/00' + str(code_id)
        o_id = id_generator()
        company = company.replace('\n', '')
        sql = u'insert into TABLE  values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9} ,{10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20})'.format(
            o_id, code_id, company, code_level, 'null', has_child, sequence, 'null', 'null', tree_code, org_level,
            status, status_time, date_from, 'null', creator, time_created, who_modified, time_modified, 'null', row_id)
        print(sql)
        code_id += 1
        sequence += 1
        l.append(sql)

    with codecs.open(company_txt, 'w', encoding='utf-8') as output_file:
        str_file = json.dumps(l, indent=4, ensure_ascii=False)
        output_file.write(str_file)

if __name__ == '__main__':
    build_insert_sql()
