pip install supervisor

supervisord 提供了一个模板文件,执行下面shell文件或者输出到文件中，改改就可以用了
echo_supervisord_conf  
#或者  
echo_supervisord_conf > supervisord.conf 


vi /root/supervisord.conf 

[program:ljtest123]
command=/usr/bin/python /root/cafe/HelloWorld/manage.py runserver 0.0.0.0:8000
autorestart=true
autostart=true
stdout_logfile=/root/ljtest.log

[supervisord]
[supervisorctl]

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[inet_http_server]   
port=127.0.0.1:9001 


[supervisord] 不写这一行会出现Error: .ini file does not include supervisord section！！！！
[supervisorctl] 不写这一行会出现Error: .ini file does not include supervisorctl section！！！

[rpcinterface:supervisor] 和 [inet_http_server] 都为使用supervisorctl所配置


supervisord <==>supervisord -c /root/supervisord.conf  



http://www.ttlsa.com/linux/using-supervisor-control-program/
