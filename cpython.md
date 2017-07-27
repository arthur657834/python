https://moonlet.gitbooks.io/cython-document-zh_cn/content/ch2-calling_c_functions.html

Cython是包含 C 数据类型的 Python
pip install cython <==> yum -y install Cython

通过静态类型提高速度
静态类型函数

compute.pyx
```python
cdef double f(double x):
    return x ** 2 - x
def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
```

setup.py
```python
from distutils.core import setup
from Cython.Build import cythonize
setup(
  name = 'Hello world app',
  ext_modules = cythonize("compute.pyx"),
)
```

test.py
```python
import compute
import time
starttime = time.clock()
compute2.integrate_f(3.2, 6.9, 1000000)
endtime = time.clock()
print "read: %f s" %(endtime - starttime)
```
python setup.py build
python setup.py install



cpdef: 对于Python可使用的函数使用（为了使得在以后的Python程序中调用Sin，Cos函数，用cpdef，而不用cdef）
cdef: 对于C可使用的函数使用

或者使用
import pyximport; pyximport.install()
就不需要setup.py了
自 Cython 0.11 起，pyximport 模块同样实验性地支持普通 Python 模块的编译了。它允许你在所有 Python import 的 .pyx 和 .py 模块上自动运行 Cython，包括哪些标准库和第三方库。但是，任然有不少 Python 模块 Cython 无法编译，遇到这种情况 import 机制（mechanism）会退回去读取 Python 原模块。.py 的 import 机制可按如下方式安装：
>>> pyximport.install(pyimport = True)

cython -a compute.py
生成html展示转化过程

cython

限制：
生成器表达式
对比char*常量
元组作为函数参数（python3已不支持）


