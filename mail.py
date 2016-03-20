from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

msg = MIMEMultipart()

att1 = MIMEText(open('d:\\test.jks', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="123.doc"'
msg.attach(att1)

att2 = MIMEText(open('d:\\2.jks', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

msg1 = MIMEText("123",_subtype='html',_charset='gb2312') 
msg.attach(msg1)

msg['to'] = '382558987@qq.com'
msg['from'] = 'kingkom7834@126.com'
msg['subject'] = 'hello world'
msg['content'] = 'hello world'
try:
    server = smtplib.SMTP()
    server.connect('smtp.126.com')
    server.login('kingkom7834','B657834')
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print 'succesful'
except Exception, e:  
    print str(e)
	