q  退出debug
h  打印可用的调试命令
b  设置断点，b 5 在第五行设置断点
h command  打印command的命令含义
disable codenum  使某一行断点失效
enable codenum   使某一行的断点有效
condition codenum xxx  针对断点设置条件
c    继续执行程序，直到下一个断点
n    执行下一行代码，如果当前语句有函数调用，则不会进入函数体中
s    执行下一行代码，但是s会进入函数
w    打印当前执行点的位置
j    codenum  让程序跳转到指定的行
l    列出附近的源码
p    打印一个参数的值
a    打印当前函数及参数的值
回车  重复执行上一行

ex1：
sum.py：
#/usr/bin/python

def add_t( ):
    i=1
    sum=0
    for i in range(1,5):
        sum=sum+i
        print sum
if __name__ == '__main__':
    add_t()
    
python -m pdb sum.py   

ex2：
import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print final
