subroutine:子程序

性能分析：分析代码和它正在使用的资源之间有什么关系

方法论：
 * 基于事件的分析 event-based profiling <==> 轨迹性能分析 tracing profiler
  * java jvmti（java tools interface）
  * .net
  * python
 * 统计式性能分析 statistical profiling
  * 分析的数据更少
  * 对性能造成的影响也更少

基于事件分析
```python
import profile
import sys

def profiler(frame,event,arg):
    print 'profiler: %r %r' %(event,arg)
sys.setprofile(profiler)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_seq(n):
    seq=[]
    if n>0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq
print fib_seq(2)
```

统计式：
```python
import profile
import datetime

tstart = None
tend = None

def start_time():
    global tstart
    tstart = datetime.datetime.now()

def get_delta():
    global tstart
    tend = datetime.datetime.now()
    delta = tend - tstart
    return delta


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

start_time()
print "About to calculate the fibonacci sequence for the number 30"
delta1 = get_delta()

start_time()
seq = fib_seq(30)
delta2 = get_delta()

print "Now we print the numbers: "
start_time()
for n in seq:
    print n
delta3 = get_delta()

print "====== Profiling results ======="
print "Time required to print a simple message: %(delta1)s" % locals()
print "Time required to calculate fibonacci: %(delta2)s" % locals()
print "Time required to iterate and print the numbers: %(delta3)s" % locals()
print "======  ======="

```
cprofile
```shell
python -m cProfile -o log.txt -s cumulative XXX.py
```
OR
```python
# -*- coding: UTF-8 -*-
def foo():
    sum = 0
    for i in range(10000):
        sum += i
    sumA = bar()
    sumB = bar()
    return sum

def bar():
    sum = 0
    for i in range(100000):
        sum += i
    return sum

if __name__ == "__main__":
    import cProfile

    #直接把分析结果打印到控制台
    cProfile.run("foo()")
    #把分析结果保存到文件中,不过内容可读性差...需要调用pstats模块分析结果
    cProfile.run("foo()", "result")
    # 增加排序方式
    #cProfile.run("test()", filename="result.out", sort="cumulative")
    #还可以直接使用命令行进行操作
    #>python -m cProfile myscript.py -o result

    import pstats
    #创建Stats对象
    p = pstats.Stats("result")
    #这一行的效果和直接运行cProfile.run("foo()")的显示效果是一样的
    p.strip_dirs().sort_stats(-1).print_stats()
    #strip_dirs():从所有模块名中去掉无关的路径信息
    #sort_stats():把打印信息按照标准的module/name/line字符串进行排序
    #print_stats():打印出所有分析信息

    #按照函数名排序
    p.strip_dirs().sort_stats("name").print_stats()

    #按照在一个函数中累积的运行时间进行排序
    #print_stats(3):只打印前3行函数的信息,参数还可为小数,表示前百分之几的函数信息
    p.strip_dirs().sort_stats("cumulative").print_stats(3)

    #还有一种用法
    p.sort_stats('time', 'cumulative').print_stats(.5, 'foo')
    #先按time排序,再按cumulative时间排序,然后打倒出前50%中含有函数信息

    #如果想知道有哪些函数调用了bar,可使用
    p.print_callers(0.5, "bar")

    #同理,查看foo()函数中调用了哪些函数
    p.print_callees("foo")

```
结果解析:
* ncalls:  函数被call的次数  如果有两列数值  第一个是总调用 第二个是原生调用
* tottime：函数总的耗时，但是不包括其子函数的耗时
* percall：tottime平均到每次调用的耗时
* cumtime：函数总的耗时，包括了其子函数的耗时（递归函数也不例外）
* percall：cumtime平均到每次调用的耗时
* filename:lineno(function) ：每个函数各自的信息

如果能够将性能分析的结果以图形的方式呈现，将会非常实用和直观，常见的可视化工具有Gprof2Dot，visualpytune，KCacheGrind等

```
什么是确定性性能分析(Deterministic Profiling)
确定性性能分析指的是反映所有的函数调用，返回，和异常事件的执行所用的时间，以及它们之间的时间间隔。相比之下，统计性性能分析指的是取样有效的程序指令，然后推导出所需要的时间，后者花费比较少的开销，但是给出的结果不够精确。

在Python中，因为其是解释性语言，所以在执行程序的时候，会加入解释器的执行，这部分的执行是不需要进行性能分析的。Python自动为每一个事件提供一个hook，来定位需要分析的代码。除此之外，因为Python解释型语言的本质往往需要在执行程序的时候加入很多其它的开销，而确定性性能分析只会加入一点点处理开销。这样一来，确定性性能分析其实开销不大，还可以提供丰富的统计信息。

函数调用次数的统计能够被用于确定程序中的bug，比如一个不符合常理的次数，明显偏多之类的，还可以用来确定可能的内联函数。函数内部运行时间的统计可被用来确定”hot loops”，那些需要运行时间过长，需要优化的部分；累积时间的统计可被用来确定比较高层次的错误，比如算法选择上的错误。Python的性能分析可以允许直接比较算法的递归实现与迭代实现的。
```

造成性能问题的一般原因：
* IO
* 内存泄露
* 未经优化的代码被平凡执行
* 密集的操作在可以缓存时未被缓存

内存泄露判断：
* 无资源加载时的内存消耗
* 线性资源加载的内存变化
* 线性资源释放的内存变化

RTC： running time complexity
* 常数时间O(1)
* 线性事件O(n)
* 对数时间O(logn) 二分查找 斐波那契数列
* 线性对数时间O(nlogn) 归并排序 堆排序 快速排序
* 阶乘O(n!)
* 平方时间O(n*n) 冒泡 插入排序 遍历二维数组

算法的时间复杂度包含三种
* 最好
* 正常
* 最坏

数据类型和操作也会影响时间复杂度

性能分析实践：
* 回归测试套件
* 思考代码结构
* 耐心
* 多收集数据
* 数据预处理 ETL
* 数据可视化

数据可视化：
方法1:
```shell
pip install pyprof2calltree
yum -y install kdesdk-kcachegrind

python -m cProfile -o myscript.cprof myscript.py
pyprof2calltree -k -i myscript.cprof
```
方法2:
```py
from xml.etree import ElementTree
from cProfile import Profile
xml_content = '<a>\n' + '\t<b/><c><d>text</d></c>\n' * 100 + '</a>'
profiler = Profile()
profiler.runctx(
    "ElementTree.fromstring(xml_content)",
    locals(), globals())
from pyprof2calltree import convert, visualize
visualize(profiler.getstats())                            # run kcachegrind
convert(profiler.getstats(), 'profiling_results.kgrind')  # save for later
```
yum -y install wxPython
pip install  SquareMap RunSnakeRun
runsnake myscript.cprof  
