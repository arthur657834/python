pip install uwsgi

vi test.py
def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return "Hello World"

uwsgi --http :8001 --wsgi-file test.py

http://10.1.50.111:8001/

django-admin.py startproject demosite
cd demosite
python manage.py runserver 0.0.0.0:8002

vi /etc/uwsgi9090.ini

[uwsgi]
socket = 127.0.0.1:9090
master = true
vhost = true
no-site = true
workers = 2
reload-mercy = 10
vacuum = true
max-requests = 1000
limit-as = 512
buffer-size = 30000
pidfile = /var/run/uwsgi9090.pid
daemonize = /tmp/uwsgi9090.log

nginx.conf:
server {
        listen       80;
        server_name  localhost;

        location / {
            include  uwsgi_params;
            uwsgi_pass  127.0.0.1:9090;
            uwsgi_param UWSGI_SCRIPT demosite.wsgi;  //入口文件，即wsgi.py相对于项目根目录的位置，“.”相当于一层目录
            uwsgi_param UWSGI_CHDIR /root/demosite;       //项目根目录
            index  index.html index.htm;
            client_max_body_size 35m;
        }
    }

	
 uwsgi --ini /etc/uwsgi9090.ini & nginx

 以下这个配置可行，上面这个不知道原因
[uwsgi]
vhost = false
plugins = python
socket = 127.0.0.1:8077
master = true
enable-threads = true
workers = 1
wsgi-file = /root/demosite/demosite/wsgi.py
#virtualenv = /root/nowamagic_venv
chdir = /root/demosite

 
 server {
        listen       80;
        server_name  10.1.50.111;
        #server_name localhost;

        access_log /tmp/access.log;
        error_log /tmp/error.log;

        #root         /root/nowamagic_venv/nowamagic_pj;
        location / {
                uwsgi_pass 127.0.0.1:8077;
                #include uwsgi_params;
                include /etc/nginx/uwsgi_params;
                #uwsgi_pass 127.0.0.1:8077;
                #uwsgi_param UWSGI_SCRIPT index;
                #uwsgi_param UWSGI_PYHOME $document_root;
                #uwsgi_param UWSGI_CHDIR  $document_root;
   }
   access_log off;
}
