# -*- coding: utf-8 -*-

#f = 'qwertasdfg'
f = open('yesterday2', 'a+', encoding='utf-8')

print(f.readline())
print(f.tell())
f.write('------------------------1\n')
print(f.tell())
f.write('------------------------\n')
print(f.tell())
f.write('------------------------\n')


#print(f.readline())
