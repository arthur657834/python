pip install django unittest-xml-reporting
mkdir cafe
cd cafe
django-admin startproject HelloWorld
cd HelloWorld
python manage.py runserver   ==> python manage.py runserver 0.0.0.0:8000

项目文件:
HelloWorld: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
HelloWorld/settings.py: 该 Django 项目的设置/配置。
HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

cd HelloWorld/HelloWorld

vi view.py:
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello world ! ")
	
vi urls.py:
from django.conf.urls import *
from HelloWorld.view import hello

urlpatterns = patterns("",
	('^hello/$', hello),
)

http://10.1.50.111:8000/hello/

templates:
mkdir templates
cd templates
vi hello.html 
<h1>{{ hello }}</h1>

vi HelloWorld/settings.py
'DIRS': [] ==> 'DIRS': [BASE_DIR+"/templates",],

vi view.py:
# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
	

lable:
if/else 标签:
{% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )，例如：

{% if condition1 %}
   ... display 1
{% elif condiiton2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}

{% if athlete_list and coach_list %}
     athletes 和 coaches 变量都是可用的。
{% endif %}

for 标签:
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}


ifequal/ifnotequal 标签:
{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}

注释标签
{# 这是一个注释 #}

include 标签
{% include "nav.html" %}



过滤器
{{ name|lower }} 文档大写转换文本为小写。
{{ my_list|first|upper }}  以上实例将第一个元素并将其转化为大写。
{{ bio|truncatewords:"30" }}  显示变量 bio 的前30个词。

addslashes : 添加反斜杠到任何反斜杠、单引号或者双引号前面。
date : 按指定的格式字符串参数格式化 date 或者 datetime 对象，实例：
{{ pub_date|date:"F j, Y" }}
length : 返回变量的长度。


模板继承:
vi base.html 
<html>
  <head>
    <title>Hello World!</title>
  </head>

  <body>
    <h1>Hello World!</h1>
    {% block mainbody %}
       <p>original</p>
    {% endblock %}
  </body>
</html>
以上代码中，名为mainbody的block标签是可以被继承者们替换掉的部分。
所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部

vi hello.html
{% extends "base.html" %}

{% block mainbody %}
<p>继承了 base.html 文件</p>
{% endblock %}



model:
vi HelloWorld/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

INSTALLED_APPS添加 'TestModel', 

python manage.py startapp TestModel

vi  TestModel/models.py
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)

以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。

python manage.py makemigrations
python manage.py migrate

注意：尽管我们没有在models给表设置主键，但是Django会自动添加一个id作为主键。

vi urls.py:
from HelloWorld.testdb import testdb
('^testdb/$', testdb),  加这两行

vi HelloWorld/testdb.py
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
	test1 = Test(name='w3cschool.cc')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")
	
http://10.1.50.111:8000/testdb/ 

获取数据:
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
	# 初始化
	response = ""
	response1 = ""
	
	
	# 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
	list = Test.objects.all()
		
	# filter相当于SQL中的WHERE，可设置条件过滤结果
	response2 = Test.objects.filter(id=1) 
	
	# 获取单个对象
	response3 = Test.objects.get(id=1) 
	
	# 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
	Test.objects.order_by('name')[0:2]
	
	#数据排序
	Test.objects.order_by("id")
	
	# 上面的方法可以连锁使用
	Test.objects.filter(name="w3cschool.cc").order_by("id")
	
	# 输出所有数据
	for var in list:
		response1 += var.name + " "
	response = response1
	return HttpResponse("<p>" + response + "</p>")
	

更新数据
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
	# 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
	test1 = Test.objects.get(id=1)
	test1.name = 'w3cschool菜鸟教程'
	test1.save()
	
	# 另外一种方式
	#Test.objects.filter(id=1).update(name='w3cschool菜鸟教程')
	
	# 修改所有的列
	# Test.objects.all().update(name='w3cschool菜鸟教程')
	
	return HttpResponse("<p>修改成功</p>")

删除数据:
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
	# 删除id=1的数据
	test1 = Test.objects.get(id=1)
	test1.delete()
	
	# 另外一种方式
	# Test.objects.filter(id=1).delete()
	
	# 删除所有数据
	# Test.objects.all().delete()
	
	return HttpResponse("<p>删除成功</p>")

	
vi  search.py 
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
	return render_to_response('search_form.html')

# 接收请求数据
def search(request):  
	request.encoding='utf-8'
	if 'q' in request.GET:
		message = '你搜索的内容为: ' + request.GET['q'].encode('utf-8')
	else:
		message = '你提交了空表单'
	return HttpResponse(message)

vi search_form.html
<html>
<head>
	<meta charset="utf-8" /> 
    <title>Search - w3cschool.cc</title>
</head>
<body>
    <form action="/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>

vi urls.py:
from HelloWorld import search
(r'^search-form/$', search.search_form),
(r'^search/$', search.search),

http://10.1.50.111:8000/search-form/

vi post.html
<html>
<head>
	<meta charset="utf-8" /> 
    <title>Search - w3cschool.cc</title>
</head>
<body>
	<form action="/search-post/" method="post">
		{% csrf_token %}
		<input type="text" name="q">
		<input type="submit" value="Submit">
	</form>

	<p>{{ rlt }}</p>
</body>
</html>

在模板的末尾，我们增加一个rlt记号，为表格处理结果预留位置。
表格后面还有一个{% csrf_token %}的标签。csrf全称是Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。POST方法提交的表格，必须有此标签。

vi HelloWorld/search2.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.context_processors import csrf

# 接收POST请求数据
def search_post(request):
	ctx ={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt'] = request.POST['q']
	return render(request, "post.html", ctx)
	
vi urls.py:	
from HelloWorld import search2
(r'^search-post/$', search2.search_post),



请求参数参考:
http://www.runoob.com/django/django-form.html

Django自动管理工具是django.contrib

vi urls.py:	
from django.contrib import admin
admin.autodiscover()
(r'^admin/', include(admin.site.urls)),

python manage.py createsuperuser 

http://10.1.50.111:8000/admin

管理模型:
vi TestModel/admin.py
from django.contrib import admin
from TestModel.models import Test
# Register your models here.
admin.site.register(Test)


vi TestModel/models.py

+
class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
		
vi TestModel/admin.py
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
		
		
自定义表单:
vi TestModel/admin.py

from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

python manage.py makemigrations
python manage.py migrate


http://10.1.50.111:8000/admin/TestModel/contact/

加入样式:
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

内联显示：
# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )
	
列表显示：
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
	search_fields = ('name',)  #增加搜索栏

