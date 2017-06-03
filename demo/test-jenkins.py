#coding=utf8
 
import httplib, urllib, urllib2, xml.dom.minidom, os,time
from cookielib import CookieJar

def printinfo( url, *vartuple ):
	resp = urllib2.urlopen(url).read();
	file_object = open('e://1.xml', 'w+')
	file_object.write(resp)
	file_object.close( )
	
	DOMTree = xml.dom.minidom.parse("e://1.xml")
	collection = DOMTree.documentElement
	for var in vartuple:
		number=DOMTree.getElementsByTagName(var)
		n1=number[0].firstChild.data
		return n1;
	os.remove("e://1.xml")

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener);

# second time do url request, the cookiejar will auto handle the cookie
loginBaiduUrl = "http://10.1.3.89:8080/hudson/j_acegi_security_check";
postData = urllib.urlencode({"j_username": "test", "j_password": "broadatest", "remember_me": "false", "from": "/hudson/"});
req = urllib2.Request(loginBaiduUrl, postData); # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.
req.add_header('Content-Type', 'application/x-www-form-urlencoded');
req.add_header('Cache-Control', 'no-cache');
req.add_header('Accept', '*/*');
req.add_header('Connection', 'Keep-Alive');
resp = urllib2.urlopen(req);
respInfo = resp.info();		

createUrl = "http://10.1.3.89:8080/hudson/view/All/createItem"
#jenkins
#create_postData=urllib.urlencode({"name": "ljtest", "mode": "hudson.maven.MavenModuleSet", "from": ""})
#hudson
create_postData=urllib.urlencode({"name": "ljtest", "mode": "hudson.maven.MavenModuleSet$DescriptorImpl", "from": "","json":'{"name": "ljtest", "mode": "hudson.maven.MavenModuleSet$DescriptorImpl", "from": ""}'})
									
req2 = urllib2.Request(createUrl, create_postData); # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.
req2.add_header('Content-Type', 'application/x-www-form-urlencoded');
req2.add_header('Cache-Control', 'no-cache');
req2.add_header('Accept', '*/*');
req2.add_header('Connection', 'Keep-Alive');
resp2 = urllib2.urlopen(req2);
respInfo2 = resp2.info();		
print respInfo2
time.sleep(30)