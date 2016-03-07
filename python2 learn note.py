#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "hello,world";
print "你好，世界";

input("1\n")
raw_input("2\n")

#string
str = 'Hello World!'
print str[2:5]
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符

#list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] #same as string
#cmp(list1, list2)
#list.append(obj)
#同count,extend扩展多值 index insert(index,obj) pop(index) sort pop remove reverse

#tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )#same as string 元组是不允许更新的
tup1 = (50,)#元组中只包含一个元素时，需要在元素后面添加逗号

#dictionary
dict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['name'] # 输出键为'name' 的值
print dict.keys() # 输出所有键
print dict.values() # 输出所有值
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典
seq = ('name', 'age', 'sex')
dict.fromkeys(seq)#{'age': None, 'name': None, 'sex': None}
dict.fromkeys(seq, 10)#{'age': 10, 'name': 10, 'sex': 10}
dict.has_key('name')
dict.items()
dict.setdefault(key, default=None)
dict.update(dict2)#添加另一个字典

#数据类型之间可以相互转换

#运算符
#//=	取整除赋值运算符
a=8.2
b=5.1
a//b #为1.0
a/b #为 1.60784313725

#比较对象，但看不出有a==b有什么区别
if ( a is b ) <=> if ( id(a) == id(b) )
	
#if
num = 5     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
else:
    print 'roadman'     # 条件均不成立时输出

#while 居然有else的用法,else在循环正常离开时才会执行 continue break  还有没什么作用的pass
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

#for 注意else的位置，跟for配套，目的是防止指数情况的重复输出
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

#以下似乎没什么用
var1 = 1
var2 = 10
del var1, var2


#不转义输出 raw
print r'\n'
print R'\n'
print "My name is %s and weight is %d kg!" % ('Zara', 21) #c 语法差不多
print "%(n)d %(x)s" % {"n":1,"x":"spam"}

#这种定义？什么用，多行？
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
</HTML>
'''

s.replace('x','y',2) //替换前两个x

#写文件
x=1
y=2
z=3
log=open('log.txt','a')
print >> log,x,y,z

#组合L1,L2，注意元素个数相对应
L1=[1,2,3,4]
L2=[5,6,7,8]
for (x,y) in zip(L1,L2):
    print (x,y,x+y)

#偏移量 好像没什么用
for (offset,item) in enumerate('abc'):
    print(item,'---',offset)

	
	
	