python -m unittest mydict_test

ex1 测试模块中的函数 :
```shell
vi myclass.py
```
```python
#!/usr/bin/env python
#encoding: utf-8
def sum( x, y):
    return x+y
def sub( x, y):
    return x-y
```

```shell
vi mytest.py
```
```python
#!/usr/bin/env python
#encoding: utf-8
import unittest
import myclass
class mytest(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass
  #具体的测试用例，一定要以test开头
  def testsum(self):
    self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
  def testsub(self):
    self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')
if __name__ =='__main__':
  unittest.main()    
```

ex2 测试模块类中的函数:
```shell
vi myclass1.py
```
```python
#!/usr/bin/env python
#encoding: utf-8
class myclass:
  def __init__(self):
    pass
  def sum(self, x, y):
    return x+y
  def sub(self, x, y):
    return x-y
```
```shell
vi mytest1.py
```
```python
#!/usr/bin/env python 
#encoding: utf-8 
import unittest 
import myclass1
class mytest(unittest.TestCase): 
  ##初始化工作 
  def setUp(self): 
    self.tclass = myclass1.myclass()
    ##实例化了被测试模块中的类 
  #退出清理工作 
  def tearDown(self): 
    pass 
  #具体的测试用例，一定要以test开头 
  def testsum(self): 
    self.assertEqual(self.tclass.sum(1, 2), 3) 
if __name__ =='__main__': 
  unittest.main()    
```  
  


  
