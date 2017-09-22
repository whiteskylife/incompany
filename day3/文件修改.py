# -*- coding: utf-8 -*-

#f = open('yesterday', 'r', encoding='utf-8')
#f_new = open('yesterday.bak', 'w', encoding='utf-8')

with open('yesterday', 'r', encoding='utf-8') as f, \
        open('yesterday.bak', 'w', encoding='utf-8') as f_new:
    for line in f.readlines():
        if '有那么多肆意的快乐等我享受' in line:
            line = line.replace('有那么多肆意的快乐等我享受', '有那么多肆意的快乐等whitesky享受')
        f_new.write(line)



