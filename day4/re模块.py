# -*- coding: utf-8 -*-
import re

# res = re.match('^Chen', 'Chenronghua123')  语法：pattern，string
# print(res)
#
# #输出：<_sre.SRE_Match object; span=(0, 4), match='Chen'>

#匹配数字相关
# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
# '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
# '$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
# '*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
# '?'     匹配前一个字符1次或0次
# '{m}'   匹配前一个字符m次
# '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
# '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
# '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c

# '\A'    效果和^是一样的，只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$
# '\d'    匹配数字0-9
# '\D'    匹配非数字
# '\w'    匹配[A-Za-z0-9]
# '\W'    匹配非[A-Za-z0-9]
# 's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
# '(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
# ?P为固定语法格式

# 注意，re的若干方法：
# match方法是从字符串开头往后匹配(用的少)
# 常用如下四种：
# search是从整个文本中搜索,匹配到一个就返回
# findall是从整个文本中搜索,贪婪匹配，如果匹配到多个全部返回，findall没有group方法
# split分隔方法
# sub替换方法

# 仅需轻轻知道的几个匹配模式
# 1.re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
# 2.M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图） [用得很少]
# 3.S(DOTALL): 点任意匹配模式，改变'.'的行为




#split方法：
# res = re.split('[0-9]+', 'abc12de3f45GH')
# print(res)
# 输出：['abc', 'de', 'f', 'GH']

#sub方法：
# res = re.sub('[0-9]+', '|', 'abc12de3f45GH', count=2)
# print(res)
# 输出：abc|de|f45GH


# 1.re.I(re.IGNORECASE): 忽略大小写
# res = re.search('[a-z]+', 'abcGH', flags=re.I)
# print(res.group())
# 输出：abcGH

# 2.M(MULTILINE): 多行模式，改变'^'和'$'的行为
# res = re.search(r"^a", "\nabc\neee", flags=re.M)
# print(res.group())
# 输出：a

# 3.S(DOTALL): 点任意匹配模式，改变'.'的行为
# res = re.search(".+", "\nabc\neee", flags=re.S)
# print(res.group())
# 输出：a


#举例：
# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行

# res = re.match('.+', 'Chen123ronghua123')
# print(res.group())
# 输出:
# Chen123ronghua123




# '$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以

#res = re.match('r.+', 'Chen123ronghua123')  #匹配结果为空，match从字符串开头开始匹配
# res = re.search('r.+', 'Chen123ronghua123')  #search 从整个文本中搜索
# print(res.group())
# 结果：ronghua



# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
# res = re.search('r[a-z]+a', 'Chen123ronghua123')  #匹配ronghua
# print(res.group())
# 结果：ronghua

# res = re.search('#.+#', '1123#hello#')
# print(res.group())
# 结果：#hello#



# '?'     匹配前一个字符1次或0次
# res0 = re.search('aal?', 'aalex')
# res1 = re.search('aal?', 'aaex')
# print(res0.group())
# print(res1.group())
# 输出
# aal
# aa



# '{m}'   匹配前一个字符m次
# res = re.search('[0-9]{3}', 'aa1xe2pp345lex')  #匹配前面的数字三次
# print(res.group())

# '{n,m}' 匹配前一个字符n到m次
# res = re.search('[0-9]{1,3}', 'aa1xe2pp345lex')  #匹配前面的数字1到3次
# print(res.group())
# 输出 1

# findall 贪婪匹配
# res = re.findall('[0-9]{1,3}', 'aa1xe2pp345lex')  #findall,贪婪匹配，匹配前面的数字1到3次
# print(res)
# 输出['1', '2', '345']             #以列表的形式返回


# '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'

# res = re.search('abc|ABC', 'ABCBabcCD')
# print(res.group())
# 输出 ABC

# res = re.findall('abc|ABC', 'ABCBabcCD')
# print(res)
# 输出 ['ABC', 'abc']




# '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c

# res = re.search('(abc){2}', 'alexabcabc')
# print(res.group())
# 输出 abcabc

# res = re.search('(abc){2}(\|\|=){2}', 'alexabcabc||=||=')   匹配||= 两次，注意需要转义
# print(res.group())
#输出：abcabc||=||=






# '\D'    匹配非数字
# res = re.search('\D+', '123$- a')
# print(res.group())
# 输出：$- a



# '\w'    匹配[A-Za-z0-9]  除了特殊字符都匹配

# res = re.search('\w+', '123$- a')
# print(res.group())
# 输出：123

# '\W'    匹配非[A-Za-z0-9]  只匹配特殊字符
# res = re.search('\W+', '123$- ...a')
# print(res.group())
# 输出：$- ...



# '\s'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
# res = re.findall('\s', '123$- \r\n\t...a')
# print(res)
# 输出：[' ', '\r', '\n', '\t']

# >>> re.search('\s+', '123$-     \r\n')
# <_sre.SRE_Match object; span=(5, 9), match=' \t\r\n'>




# '\A'    效果和^是一样的，只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$
# '\d'    匹配数字0-9

# 例：
# res = re.search('\A[0-9]+[a-z]\Z', '123a')
# print(res.group())
# 输出:123a


#* : 0个至多个
#+ ：1个至多个

# res = re.match('^Chen\d+', 'Chen123ronghua123')
# print(res)
# print(res.group())              #查看匹配到的对象

#输出：<_sre.SRE_Match object; span=(0, 7), match='Chen123'>
# Chen123




#'(?P<name>...)' 分组匹配
# res = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
# print(res)
# 结果{'province': '3714', 'city': '81', 'birthday': '1993'}


