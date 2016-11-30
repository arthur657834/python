pip install mock

Mock 类定义:
class Mock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, \*\*kwargs)

Mock对象的一般用法是这样的：

找到你要替换的对象，这个对象可以是一个类，或者是一个函数，或者是一个类实例。
然后实例化Mock类得到一个mock对象，并且设置这个mock对象的行为，比如被调用的时候返回什么值，被访问成员的时候返回什么值等。
使用这个mock对象替换掉我们想替换的对象，也就是步骤1中确定的对象。
之后就可以开始写测试代码，这个时候我们可以保证我们替换掉的对象在测试用例执行的过程中行为和我们预设的一样。

module.py:
```python
class Count():

    def add(self, a, b):
        return a + b
```

mock_demo.py:
```python
from unittest import mock
import unittest
from module import Count


class MockDemo(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
```

count.add = mock.Mock(return_value=13, side_effect=count.add)

side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。

count.add.assert_called_with(8, 8)
检查mock方法是否获得了正确的参数。

function.py:
```python
def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)


def multiply(x, y):
    return x * y
```

func_test.py:
```python
import unittest
from unittest.mock import patch
import function


class MyTestCase(unittest.TestCase):

    @patch("function.multiply")
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = function.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()
```

@patch("function.multiply")
patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。

def test_add_and_multiply2(self, mock_multiply):

　　在定义测试用例中，将mock的multiply()函数（对象）重命名为 mock_multiply对象。

mock_multiply.return_value = 15

　　设定mock_multiply对象的返回值为固定的15。
