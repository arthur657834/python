[reference documentation](https://doc.scrapy.org/en/latest/intro/install.html)

[reference documentation chiniese](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html#id3)
``` shell
yum -y install openssl-devel

pip install Scrapy

scrapy startproject p1
```

[root@localhost tutorial]# tree
.
├── scrapy.cfg #-------------------项目配置文件  
└── tutorial
    ├── __init__.py
    ├── items.py  #-------项目数据字段文件  
    ├── middlewares.py
    ├── pipelines.py #-------项目管道文件
    ├── settings.py #---------项目配置文件
    └── spiders #----------项目存放蜘蛛的目录
        ├── __init__.py
        └── quotes_spider.py

 item.py：项目数据字段文件，定义需要的数据段，这些字段即为爬取下来数据中提取的，可以通过定义Item类实现
 ```py
 import scrapy

 class DmozItem(scrapy.Item):
     title = scrapy.Field()
     link = scrapy.Field()
     desc = scrapy.Field()
 ```

pipeline.py：管道文件，接收item各字段对应数据，放到数据库mongodb或mysqldb

vi quotes_spider.py
``` python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        #allowed_domains = ["toscrape.com"]
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
    def parse(self, response):
                for sel in response.xpath('//ul/li'):
                    item = DmozItem()
                    item['title'] = sel.xpath('a/text()').extract()
                    item['link'] = sel.xpath('a/@href').extract()
                    item['desc'] = sel.xpath('text()').extract()
                    yield item
```       

scrapy crawl quotes --nolog -o items.json

Selector有四个基本的方法(点击相应的方法可以看到详细的API文档):

* xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表 。
* css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表.
* extract(): 序列化该节点为unicode字符串并返回list。
* re(): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表。

scrapy shell 'http://quotes.toscrape.com/page/1/'
response.body
response.headers
response.xpath('//ul/li/text()').extract()
response.selector.css() <==> response.css()
response.selector.xpath() <==> response.xpath()
