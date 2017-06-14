```shell
pip install virtualenv
#--system-site-packages 使用系统模块或包
virtualenv --system-site-packages env

pip install virtualenvwrapper
export WORKON_HOME=/root/python_vir
source /usr/bin/virtualenvwrapper.sh
```
```
创建环境
mkvirtualenv env1            --python=/usr/bin/python2.7

切换环境
workon env1

列出已有环境
workon

退出环境
deactivate

删除环境
rmvirtualenv

创建project
项目将创建到PROJECT_HOME目录下，实际上相当于在某个目录下，建了一个环境。
mkproject
```
