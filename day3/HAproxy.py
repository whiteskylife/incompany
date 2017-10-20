# -*- coding: utf-8 -*-
import json
import re

# data = {'a': [1, 2.0, 3, 4],    'b': ("character string", "byte string"),    'c': 'abc'}
#
# du = json.dumps(data)
# print(du)
# print(json.loads(du))

# with open('data.json','w') as f:
#     json.dump(data,f,indent=2,sort_keys=True,separators=(',',':'))
#     f.write(json.dumps(data))
#     with open('data.json','r') as f:
#         data = json.load(f)
#         print(repr(data))


def backup_file():
    with open('HAproxy.txt', 'r') as ori:
        with open('HAproxy.txt.bak', 'w') as bak:
            for line in ori:
                bak.write(line)

#backup_file()


def search_fun():
    backend_list = []
    flag = False
    search_content = input('what do you want to search: ')
    with open('HAproxy.txt', 'r') as file:
        for line in file:
            if line.strip() == 'backend %s' % search_content:
                flag = True
                print(line.strip())
                continue
            if line.strip().startswith('backend'):
                flag = False
            if flag and line.strip():
                print(line.strip())
                backend_list.append(line.strip())
        print(backend_list)
#search_fun()


def judge_ip(input_ip):
    p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
    if re.match(p, input_ip):
        return True
    else:
        return False

a = judge_ip(input('plz input ip: '))
print(a)


def add_fun():
    backend = str(input('plz input backend name: '))
    server_ip = str(input('plz input server ip: '))
    weight = int(input('plz input weight: '))
    maxconn = int(input('plz input maxconn: '))
    record = 'server %s weight %d maxconn %s' % (server_ip, weight, maxconn)

    judge_ip(server_ip)

    with open('HAproxy.txt', 'r+') as file:
        for line in file:
            if re.search(backend, line):
                print('the backend name is in use')
                return 'backend name in use'
        file.write('\n\nbackend %s\n\t\t %s' % (backend, record))

# a = add_fun()
# print(a)
