import IPy  
IPy.IP('10.0.0.0/8').version()  
IPy.IP('::1').version() 
print IPy.IP(0x7f000001) 
print IPy.IP('127.0.0.1')  
print IPy.IP('127.0.0.0/255.0.0.0') 
print IPy.IP('127.0.0.0-127.255.255.255')  
print IPy.IP('10') 
print IPy.IP('1080:0:0:0:8:800:200C:417A')  
print IPy.IP('::1') 

print IPy.IP('10.0.0.0/24').strNormal(0)#0-4 

print IPy.IP('172.29.20.0/24').strNetmask()
print '127.0.0.1' in IPy.IP('127.0.0.0/24')

print (IPy.IP('192.168.1.1').strHex())
print (IPy.IP('192.168.1.1').int())
print (IPy.IP('192.168.1.1').strBin())

print (IPy.IP('192.168.1.0').make_net('255.255.255.0'))
print IPy.IP('192.168.1.0/255.255.255.0',make_net=True)
print IPy.IP('192.168.1.0-192.168.1.255',make_net=True)

print IPy.IP('10.0.0.0/22')>IPy.IP('12.0.0.0/22')

print IPy.IP('192.168.0.0/23').overlaps('192.168.1.0')
print IPy.IP('192.168.0.0/23').overlaps('192.168.1.0/24')
