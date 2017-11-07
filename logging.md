```
format参数中可能用到的格式化串： 
%(name)s Logger的名字 
%(levelno)s 数字形式的日志级别 
%(levelname)s 文本形式的日志级别 
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有 
%(filename)s 调用日志输出函数的模块的文件名 
%(module)s 调用日志输出函数的模块名 
%(funcName)s 调用日志输出函数的函数名 
%(lineno)d 调用日志输出函数的语句所在的代码行 
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示 
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数 
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 
%(thread)d 线程ID。可能没有 
%(threadName)s 线程名。可能没有 
%(process)d 进程ID。可能没有 
%(message)s用户输出的消息
```
ex1:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
logger.info('Start reading database')
# read database here
 
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
 
logger.info('Finish updating records')
```
ex2:
```python
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
 
# create a file handler
 
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
 
# create a logging format
 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
 
# add the handlers to the logger
 
logger.addHandler(handler)
 
logger.info('Hello baby')
```
ex3:
```python
import logging
import logging.config
 
logger = logging.getLogger(__name__)
 
# load config from file 
 
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
 
# or, for dictConfig
 
logging.config.dictConfig({
    'version': 1,              
    'disable_existing_loggers': False,  # this fixes the problem
 
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',    
            'class':'logging.StreamHandler',
        },  
    },
    'loggers': {
        '': {                  
            'handlers': ['default'],        
            'level': 'INFO',  
            'propagate': True  
        }
    }
})
 
logger.info('It works!')
```

logging.json
```json

{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
 
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
 
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
 
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
 
    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },
 
    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler", "error_file_handler"]
    }
}
```

logging.yaml
```yaml
version: 1
 
disable_existing_loggers: False
 
formatters:
 
    simple:
 
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
 
handlers:
 
    console:
 
        class: logging.StreamHandler
 
        level: DEBUG
 
        formatter: simple
 
        stream: ext://sys.stdout
 
    info_file_handler:
 
        class: logging.handlers.RotatingFileHandler
 
        level: INFO            
 
        formatter: simple
 
        filename: info.log
 
        maxBytes: 10485760 # 10MB
 
        backupCount: 20
 
        encoding: utf8
 
    error_file_handler:
 
        class: logging.handlers.RotatingFileHandler
 
        level: ERROR            
 
        formatter: simple
 
        filename: errors.log
 
        maxBytes: 10485760 # 10MB
 
        backupCount: 20
 
        encoding: utf8
 
loggers:
 
    my_module:
 
        level: ERROR
 
        handlers: [console]
 
        propagate: no
 
root:
 
    level: INFO
 
    handlers: [console, info_file_handler, error_file_handler]
```
ex4:
```python
import json
import logging.config
 
def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration
 
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
            #config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
```
ex5:
```python
#!/usr/bin/env python
#_*_coding:utf-8_*_
# vim : set expandtab ts=4 sw=4 sts=4 tw=100 :

import logging
import time
import re
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def main():
    #日志打印格式
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)
    #创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename="ds_update", when="M", interval=2, backupCount=2)
    #log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    #log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)    
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.addHandler(log_file_handler)
    #循环打印日志
    log_content = "test log"
    count = 0
    while count < 30:
        log.error(log_content)
        time.sleep(20)
        count = count + 1
    log.removeHandler(log_file_handler)


if __name__ == "__main__":
    main()
```
```
filename：日志文件名的prefix；
when：是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下： 
“S”: Seconds 
“M”: Minutes 
“H”: Hours 
“D”: Days 
“W”: Week day (0=Monday) 
“midnight”: Roll over at midnight
interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件；
backupCount: 表示日志文件的保留个数；
除了上述参数之外，TimedRotatingFileHandler还有两个比较重要的成员变量，它们分别是suffix和extMatch。suffix是指日志文件名的后缀,suffix中通常带有格式化的时间字符串，filename和suffix由“.”连接构成文件名（例如：filename=“runtime”， suffix=“%Y-%m-%d.log”,生成的文件名为runtime.2015-07-06.log）。extMatch是一个编译好的正则表达式，用于匹配日志文件名的后缀，它必须和suffix是匹配的，如果suffix和extMatch匹配不上的话，过期的日志是不会被删除的。比如，suffix=“%Y-%m-%d.log”, extMatch的只应该是re.compile(r”^\d{4}-\d{2}-\d{2}.log$”)。默认情况下，在TimedRotatingFileHandler对象初始化时，suffxi和extMatch会根据when的值进行初始化： 
‘S’: suffix=”%Y-%m-%d_%H-%M-%S”, extMatch=r”\^d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}”； 
‘M’:suffix=”%Y-%m-%d_%H-%M”,extMatch=r”^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}”; 
‘H’:suffix=”%Y-%m-%d_%H”,extMatch=r”^\d{4}-\d{2}-\d{2}_\d{2}”; 
‘D’:suffxi=”%Y-%m-%d”,extMatch=r”^\d{4}-\d{2}-\d{2}”; 
‘MIDNIGHT’:”%Y-%m-%d”,extMatch=r”^\d{4}-\d{2}-\d{2}”; 
‘W’:”%Y-%m-%d”,extMatch=r”^\d{4}-\d{2}-\d{2}”; 
如果对日志文件名没有特殊要求的话，可以不用设置suffix和extMatch，如果需要，一定要让它们匹配上。
```
```
logger.error('Failed to open file', exc_info=True)<==>logger.exception(msg, _args)
使用参数 exc_info=true 调用 logger 方法, traceback 会输出到 logger 中

使用 __name__ 作为 logger 的名称

虽然不是非得将 logger 的名称设置为 __name__ ，但是这样做会给我们带来诸多益处。在 python 中，变量 __name__ 的名称就是当前模块的名称。比如，在模块 “foo.bar.my_module” 中调用 logger.getLogger(__name__) 等价于调用logger.getLogger(“foo.bar.my_module”) 。当你需要配置 logger 时，你可以配置到 “foo” 中，这样包 foo 中的所有模块都会使用相同的配置。当你在读日志文件的时候，你就能够明白消息到底来自于哪一个模块。
```
