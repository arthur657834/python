test:
	dir:
		b.py
		__init__.py  发现要包含目录下的文件时需要在目录下声明一个__init__.py文件，即使这个文件是空的也可以
	a.py

a.py:
import dir.b
print dir.b.name

import 上级目录:
import sys
sys.path.append("..")
import mod1


from home.a.b import *   前提 home、a中都包括__init__.py

sys.path.append("/home/a/")




