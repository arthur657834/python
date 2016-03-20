import wmi
import time
logfile = 'logs_%s.txt' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
def call_remote_bat(ipaddress,username,passwd):
    try:
        conn = wmi.WMI(computer=ipaddress,user=username,password=passwd)
        filename=r"C:\1.bat"   
        cmd_callbat=r"start %s"%filename
        conn.Win32_Process.Create(CommandLine=cmd_callbat)  
        print "successful!"
        return True
    except Exception,e:
        log = open(logfile, 'a')
        log.write(('%s, call bat Failed!\r\n') % ipaddress)
        log.close()
        return False
    return False

if __name__=='__main__':
    call_remote_bat("10.1.241.88","administrator","broada@123")