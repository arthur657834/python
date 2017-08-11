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
logger.error('Failed to open file', exc_info=True)<==>logger.exception(msg, _args)
使用参数 exc_info=true 调用 logger 方法, traceback 会输出到 logger 中



使用 __name__ 作为 logger 的名称

虽然不是非得将 logger 的名称设置为 __name__ ，但是这样做会给我们带来诸多益处。在 python 中，变量 __name__ 的名称就是当前模块的名称。比如，在模块 “foo.bar.my_module” 中调用 logger.getLogger(__name__) 等价于调用logger.getLogger(“foo.bar.my_module”) 。当你需要配置 logger 时，你可以配置到 “foo” 中，这样包 foo 中的所有模块都会使用相同的配置。当你在读日志文件的时候，你就能够明白消息到底来自于哪一个模块。

