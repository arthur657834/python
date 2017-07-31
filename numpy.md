出现原因：
* Python中提供了list容器，可以当作数组使用。但列表中的元素可以是任何对象，因此列表中保存的是对象的指针，这样一来，为了保存一个简单的列表[1,2,3]。就需要三个指针和三个整数对象。对于数值运算来说，这种结构显然不够高效。
* Python虽然也提供了array模块，但其只支持一维数组，不支持多维数组，也没有各种运算函数。因而不适合数值运算。


Numpy基础部分中，有两个主要内容，如下：
* 任意维数的数组对象（ndarray，n-dimensional array object）
* 通用函数对象（ufunc，universal function object）

NumPy数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推。在NumPy中，每一个线性的数组称为是一个轴（axes），秩其实是描述轴的数量。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是NumPy中的轴（axes），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。

NumPy的数组中比较重要ndarray对象属性有：

* ndarray.ndim：数组的维数（即数组轴的个数），等于秩。最常见的为二维数组（矩阵）。
* ndarray.shape：数组的维度。为一个表示数组在每个维度上大小的整数元组。例如二维数组中，表示数组的“行数”和“列数”。ndarray.shape返回一个元组，这个元组的长度就是维度的数目，即ndim属性。
* ndarray.size：数组元素的总个数，等于shape属性中元组元素的乘积。
* ndarray.dtype：表示数组中元素类型的对象，可使用标准的python类型创建或指定dtype。另外也可使用前一篇文章中介绍的NumPy提供的数据类型。
* ndarray.itemsize：数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(float64占用64个bits，每个字节长度为8，所以64/8，占用8个字节），又如，一个元素类型为complex32的数组item属性为4（32/8）。
* ndarray.data：包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

当arange使用浮点数参数时，由于浮点数精度有限，通常无法预测获得的元素个数。因此，最好使用函数linspace去接收我们想要的元素个数来代替用range来指定步长。
numpy.linspace(-1, 0, 5)

>>> a = arange(9).reshape(3,3)  
>>> a  
array([[0, 1, 2],  
           [3, 4, 5],  
           [6, 7, 8]])  
>>> b = 2 * a  
>>> b  
array([[ 0, 2, 4],  
       [ 6, 8, 10],  
       [12, 14, 16]])  


水平组合
hstack((a, b)) <==> concatenate((a, b), axis=1) 
array([[ 0, 1, 2, 0, 2, 4],  
       [ 3, 4, 5, 6, 8, 10],  
       [ 6, 7, 8, 12, 14, 16]])  
垂直组合
vstack((a, b)) <==> concatenate((a, b), axis=0) 
深度组合
dstack((a, b)) <==> [a1,b1],[a2,b2]
array([[[ 0, 0],  
        [ 1, 2],  
        [ 2, 4]],  
  
       [[ 3, 6],  
        [ 4, 8],  
        [ 5, 10]],  
  
       [[ 6, 12],  
        [ 7, 14],  
        [ 8, 16]]])  

列组合
column_stack((a, b)) 

行组合
row_stack

>>> a = arange(9).reshape(3,3)  
>>> a  
array([[0, 1, 2],  
       [3, 4, 5],  
       [6, 7, 8]])  
>>> hsplit(a, 3)  <==> split(a, 3, axis=1) 
[array([[0],  
       [3],  
       [6]]),  
 array([[1],  
       [4],  
       [7]]),  
 array([[2],  
       [5],  
       [8]])] 

vsplit(a, 3) <==> split(a, 3, axis=0)

dsplit(c, 3) 

完全不复制:
>>> a = arange(12)  
>>> b = a      #不创建新对象  
>>> b is a           # a和b是同一个数组对象的两个名字  
True  
>>> b.shape = 3,4    #也改变了a的形状  
>>> a.shape  
(3, 4)  

视图(view)和浅复制
不同的数组对象分享同一个数据。视图方法创造一个新的数组对象指向同一数据。
>>> c = a.view()  
>>> c is a  
False  
>>> c.base is a      #c是a持有数据的镜像  
True  
>>> c.flags.owndata  
False  
>>>  
>>> c.shape = 2,6    # a的形状没变  
>>> a.shape  
(3, 4)  
>>> c[0,4] = 1234        #a的数据改变了  
>>> a  
array([[   0,    1,    2,    3],  
       [1234,    5,    6,    7],  
       [   8,    9,   10,   11]]) 
       
深复制:
d = a.copy()       #创建了一个含有新数据的新数组对象


ex1:
```python
ones( (2,3,4), dtype=int16 ) # 2个3*4的数组
empty((3,4))
zeros((3,4))
# 默认创建的数组类型(dtype)都是float64 ，8字节

```
ex2:
```
arange(10, 30, 5) 
返回一个数列形式的数组:array([10, 15, 20, 25]) 

numpy.linspace(-1, 0, 5) ==> array([-1.  , -0.75, -0.5 , -0.25,  0.  ])  

arange(7, dtype=uint16) ==> array([0, 1, 2, 3, 4, 5, 6], dtype=uint16) 

set_printoptions(threshold='nan') 
强制NumPy打印整个数组

```

ex3:
```
student= dtype({'names':['name', 'age', 'weight'], 'formats':['S32', 'i','f']}, align = True)  
这里student是自定义结构类型的名称，使用dtype函数创建，在第一个参数中，'names'和'formats'不能改变，names中列出的是结构中字段名称，formats中列出的是对应字段的数据类型。S32表示32字节长度的字符串，i表示32位的整数，f表示32位长度的浮点数。最后一个参数为True时，表示要求进行内存对齐。

a= array([(“Zhang”, 32, 65.5), (“Wang”, 24, 55.2)], dtype =student)
```


