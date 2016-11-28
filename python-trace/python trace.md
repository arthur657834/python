yum -y install graphviz graphviz-devel
pip install pygraphviz

因为take_frame需要传参指定生成的图片名，所以我实际使用时把这个cheese.py重命名为_cheese.py，另起一个cheese.py对其做传参调用。
你可以生成一张采集grains时的执行过程图，在一个grains功能函数中导入这个模块并执行take_frame就行了，通过关键字参数指定输出图片名take_frame(out='xxx.png')

cd /srv/salt/_grains/

_cheese.py

vi ljtest.py
def testfunc():
    import _cheese
    _cheese.take_frame(out='/root/take_frame1.png')
    grains = {}
    grains['single'] = 'single_value'
    grains['list'] = ['list_value1', 'list_value2']
    grains['dict'] = {'key1': 'value1', 'key2': 'value2'}
    return grains
 
def _anotherfunc():
    import _cheese
    _cheese.take_frame(out='/root/take_frame2.png')
    grains = {}
    grains['anotherfunc'] = 'anotherfunc'
    return grains

执行salt '*' grains.items 即可产生





