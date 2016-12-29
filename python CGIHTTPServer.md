ex1:
#!/usr/bin/env python
print "200 OK"
print "Content-Type:text/html"
print ""

print "hello world!"

ex2:
#!/bin/bash
echo "Content-Type:text/html"
echo ""

echo "hello world!"

ex3:
text.html
<!DOCTYPE HTML>  
<html>  
    <head>  
        <title>  
            hello python cgi  
        </title>  
    </head>  
    <body>  
    <p>test for python cgi server</p>  
        <form action="/cgi-bin/form.py">              
            <label for="">text:</label><input type="text" name="text" value = "test">  
            <input type="submit">  
        </form>  
    </body>  
</html>

form.py:
# -*- coding: utf-8 -*-
            
import cgi
            
header = 'Content-Type: text/html\n\n'
            
html = '<h3>接受处理表单数据\n</h3>'
#打印返回的内容
print header
print html
# 接受表达提交的数据
form = cgi.FieldStorage()
            
print '接收表达get的数据 ：',form  
            
print '<p />'
            
# 解析处理提交的数据
content = form['text'].value
            
formhtml = '''
<label for="">you say:</label><input type="text" value="%s">
'''
            
print formhtml % (content)
#ex3 有错待查

python -m CGIHTTPServer  (8888)

http://10.1.50.250:8000/cgi-bin/3.py
http://10.1.50.250:8000/cgi-bin/3.sh
http://10.1.50.250:8000/cgi-bin/test.html

