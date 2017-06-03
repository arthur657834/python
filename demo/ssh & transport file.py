#!/usr/bin/python

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.100.4",22,"root", "12345678")
stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.readlines()
ssh.close()

t = paramiko.Transport(("192.168.100.4",22))
t.connect(username = "root", password = "12345678")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/tmp/test.txt'
localpath='/tmp/yum.log'
sftp.put(localpath,remotepath)
t.close()

t = paramiko.Transport(("192.168.100.4",22))
t.connect(username = "root", password = "12345678")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/tmp/test.txt'
localpath='/tmp/test.txt'
sftp.get(remotepath, localpath)
t.close()

