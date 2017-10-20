# -*- coding: utf-8 -*-


import requests
import s1
from xml.etree import ElementTree as ET

# xml
# root = ET.XML(open('first.xml', 'r', encoding='utf-8').read())
# print(root.tag)
#
# for node in root:
#     print(node.tag, node.attrib, node.find('year').text)   # 新的node节点：year，如果year中嵌套了其他子节点，其他子节点仍然有tag，attrib，text等属性

tree = ET.parse('first.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)
print(root.text)

# 创建节点,在创建的son节点中增加grandson节点
# son = root.makeelement('tt', {'kk': 'vv'})
# grandson = son.makeelement('yy', {'mm': '666666'})
# son.append(grandson)
# root.append(son)  # 追加到xml主节点最后

# 另一种方法创建节点
son = ET.Element('pp', {'ss': 'dd'})
ele2 = ET.Element('pp', {'ss': '123123'})
son.append(ele2)
root.append(son)
tree.write('out.xml')
