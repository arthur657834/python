pip install -U pytest
py.test --version

ex1:
vi test_example.py
#coding=utf-8

# 功能
def func(x):
    return x + 1

# 测试用例
def test_answer():
    assert func(3) == 5
    
py.test 执行单元测试

ex2:
vi test_class.py
#coding=utf-8

class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hi"
        
py.test -q test_class.py 执行单元测试

ex3:
vi test_mian.py
import pytest

def test_main():
    assert 5 != 5

if __name__ == '__main__':
    pytest.main()
    #pytest.main("-q test_main.py")指定测试文件  不生效
    #pytest.main("/root")  # 指定测试目录 不生效
py.test 执行当前文件夹下的所有文件的单元测试    
        
ex4:
有时候我们的测试用例文件分散在不同的层级目录下，通过命令行的方式运行测试显示不太方便，如何编写一个运行所有测试用例的脚本呢？ pytest可以自动帮我们生成这样的脚本。
py.test --genscript=runtests.py
python runtest.py



