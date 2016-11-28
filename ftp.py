#-*- coding: utf-8 -*-  
  
import ftplib 
  
def ftpconnect():
    ftp_server = '10.1.50.252'  
    username = 'administrator'  
    password = 'Broada_123!'  
    ftp=FTP()  
    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息  
    ftp.connect(ftp_server,21) #连接  
    ftp.login(username,password) #登录，如果匿名登录则用空串代替即可  
    return ftp  
      
def downloadfile():
    remotepath = "/releases/delivery/cloudone-all-1.0.0.M1-SNAPSHOT.zip";  
    ftp = ftpconnect()  
    print ftp.getwelcome() #显示ftp服务器欢迎信息  
    bufsize = 1024 #设置缓冲块大小  
    localpath = 'C:\\Users\\lj\\Desktop\\tmp\\cloudone-all-1.0.0.M1-SNAPSHOT.zip'  
    fp = open(localpath,'wb') #以写模式在本地打开文件  
    ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize) #接收服务器上文件并写入本地文件  
    ftp.set_debuglevel(0) #关闭调试  
    fp.close()  
    ftp.quit() #退出ftp服务器  

def uploadfile():  
  
    remotepath = "/releases/delivery/1.xml"  
    ftp = ftpconnect()  
    bufsize = 1024  
    localpath = 'E:\\1.xml'  
    fp = open(localpath,'rb')  
    ftp.storbinary('STOR '+ remotepath ,fp,bufsize) #上传文件  
    ftp.set_debuglevel(0)  
    fp.close() #关闭文件  
    ftp.quit()  
	
downloadfile()
uploadfile()  



	