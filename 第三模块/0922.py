# -*- coding: utf-8 -*-


import pickle

test = [1, 2]


def change(inner_list=[]):
    inner_list += [2, 3]

change(test)

pickle.dump(test, open('test_pickle_file', 'wb'))
print(pickle.load(open('test_pickle_file', 'rb')))

# 输出 [1, 2, 2, 3]