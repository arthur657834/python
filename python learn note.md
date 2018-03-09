http://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/
```
指定编码
# -*- coding: cp-1252 -*-
# -*- coding:utf-8 -*- 

这句是告诉python程序中的文本是utf-8编码，让python可以按照utf-8读取程
字符串前面加r，表示的意思是禁止字符串转义
中文前加u就是告诉python后面的是个unicode编码，存储时按unicode格式存储。

```
```
标识符
第一个字符必须是字母表中字母或下划线'_'
在Python 3中，非-ASCII 标识符也是允许的了。

python保留字
import keyword
keyword.kwlist
```

### 字符串
```
python中单引号和双引号使用完全相同。
使用三引号('''或""")可以指定一个多行字符串。
转义符 '\'
自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
字符串是不可变的。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
s = 'Yes,he doesn\'t'
print(s, type(s), len(s))
print(word[0], word[-5])  word[1:5] word[5:]
print('my'*3) =>mymymy
print("""\ \的作用是避免在最开始产生一个不需要的空行
	Usage: thingy [OPTIONS]
	-h                        Display this usage message
	-H hostname               Hostname to connect to
""")
```

### Numbers
```
a, b, c, d = 20, 5.5, True, 4+3j
```

### List（列表）
```
a = ['him', 25, 100, 'her']
a + [6, 7, 8]
a[2:5] = []  # 删除
cubes.append(216)
del a[2:4]
	
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。
```

### Tuple（元组）
```
a = (1991, 2014, 'physics', 'math')
构造包含0个或1个元素的tuple是个特殊的问题，所以有一些额外的语法规则：
tup1 = () # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
tup1+tup2
```

### Sets（集合）
```
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
'Rose' in student  # membership testing（成员测试） =>true
a = set('abracadabra')
b = set('alacazam')
a-b # a和b的差集
a | b # a和b的并集
a & b     # a和b的交集
a ^ b     # a和b中不同时存在的元素
```

### Dictionaries（字典）
```
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)
tel['Jack']
del tel['Rose']
tel['Mary'] = 4127
list(tel.keys())
sorted(tel.keys()
'Mary' not in tel  # 成员测试
for k, v in knights.items():
```

Tips:
```
第一行如下,可像shell 一下执行 ./hello.py
#! /usr/bin/env python3.4	


round(113.0625, 2)  113.06

在交互模式中，最后被输出的表达式结果被赋值给变量 _ 
```

基础：
```python
age = int(input("Age of the dog: "))

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
	
while 判断条件：
    statements
	
for <variable> in <sequence>:
	<statements>
else:
	<statements>

for i in range(0, 10, 3) :
	print(i)

while True:
	pass  # 等待键盘中断 (Ctrl+C)
	
def return_sum(x,y):
    c = x + y
    return c
```

判断是否为主模块
```
if __name__ == '__main__':
	print('程序自身在运行')
```

导入子模块
```python
import sound.effects.echo
from sound.effects import echo	
```

str() 函数返回一个用户易读的表达形式。<br>
repr() 产生一个解释器易读的表达形式。<br>
rjust() 可以将字符串靠右, 并在左边填充空格。<=>ljust() 和 center()<br>
zfill() 在数字的左边填充 0<br>

str.format()
ex.   
```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
```

reload

exec(open('script.py').read())

random.random()
random.choice([1,2,3,4])
random.randint(1,10)

s.find("test")
s.replace("test","lj")
s.rstrip()#去除右边的换行符D

'%s ,eggs.and %s' % ('test1','test2')
'{0} ,eggs.and {1}'.format('test1','test2')

dir(变量名)#输出可用的方法
help(s.find)

col=[row[1] fro row in M]#M的第二列组成新的的列表
G=(sum(row) for row in M)

value=d['x'] if 'x' in d else 0;

if type(L)==type([]):
if type(L)==list:
if isinstance(L,list):

Fraction('.25')+Fraction('1.25')<=>Fraction('1.5')

open(r'c:\test','w')<=>open('c:\\test','w')


print 5.5/2  ==> 2.75
print 5.5//2 ==> 2.0

DocStrings:
```python
#!/usr/bin/python
# Filename: func_doc.py
# Date：2011-09-07 
# Author：Chris
 
def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__
```
$ python func_doc.py
5 is maximum
Prints the maximum of two numbers.

        The two values must be integers.

赋予doc属性	
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
	
python 有对接jira的库

distribute是setuptools的替代方案，pip是easy_install的替代方案

Distribute提供一个安装python模块的框架

pip install distribute

--distribute 选项使virtualenv使用新的基于发行版的包管理系统而不是 setuptools 获得的包。 你现在需要知道的就是 --distribute 选项会自动在新的虚拟环境中安装 pip

export VIRTUALENV_USE_DISTRIBUTE=true python版本兼容设置
PIP_DOWNLOAD_CACHE=/root/.pip-cache tip:如无法接入internet也会安装失败



pip install nose coverage

Mercurial plugin
Cobertura Plugin
Task Scanner Plug-in


nosetests --where . --with-xunit --xunit-file=nosetests.xml

nosetests --with-xunit --with-coverage && coverage xml



pip freeze > requirement.txt
pip install -r requirement.txt

pip bundle -r requirement.txt ljtest.pybundle
pip install ljtest.pybundle


pip install mercurial
mercurial 跟git相似

pip install pep8 pyflakes
pep8 编码风格检测
pyflakes 语法检测
pep8/pyflakes 1.py


python -m zipfile -e 1.zip 


pip install trac
trac-admin ljtest initenv
tracd -s --port 8000 ljtest

htpasswd -c ljtest/trac.htpasswd admin
htpasswd  ljtest/trac.htpasswd king

tracd -s --port 8000 --basic-auth="ljtest,ljtest/trac.htpasswd,Ljtest" ljtest
工程路径 密码文件路径 工作域名

ticket


https://www.dropbox.com/

tip1:
python xxx.py
python -m xxx.py
1、叫做直接运行
2、相当于import,叫做当做模块来启动
不同的加载py文件的方式，主要是影响——sys.path 这个属性。sys.path 就相当于liunx中的PATH。
测试文件:

```python
import sys
sys.path
```

直接启动是把run.py文件，所在的目录放到了sys.path属性中。
模块启动是把你输入命令的目录（也就是当前路径），放到了sys.path属性中***

可以分析代码使用
```shell
python -m dis 1.py
```

ex1:
```python
s=[1,2,3,4,5,6]
i=0
i=s[i]=3

i=3
s=[1,2,3,3,5,6]
```
