# -*- coding: utf-8 -*-
# def backup():
#     with open('haproxy配置文件', 'r+', encoding='utf-8') as config_file:
#         with open('haproxy配置文件.bak', 'a+', encoding='utf-8') as config_file.bak:
#             for line in config_file:
#                 config_file.bak.write(line)
# backup()
import re

p = re.compile(r'\d+')
w = p.finditer('12 qweasd23ees qwezxcdsa, 324 ... 12 ...')

for match in w:
    match.group()

p.match()
