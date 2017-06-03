import dns.resolver

A=dns.resolver.query("www.qq.com",'A')
for i in A.response.answer:
	for j in i.items:
		print j.address
		
MX=dns.resolver.query("126.com",'MX')
for i in MX:
	print i.preference,i.exchange

NS=dns.resolver.query("126.com",'NS')	
for i in NS.response.answer:
	for j in i.items:
		print j.to_text()

CNAME=dns.resolver.query("www.qq.com",'CNAME')	
for i in NS.response.answer:
	for j in i.items:
		print j.to_text()