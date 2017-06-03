import wmi

# connection = wmi.connect_server(
#   server="10.1.241.88",
#   user="administrator",
#   password="broada@123"
# )
# c = wmi.WMI(wmi=connection)

c = wmi.WMI(
  computer="10.1.241.88",
  user="administrator",
  password="broada@123"
)

print "process list-------------------------"
for process in c.Win32_Process():
  print process.ProcessId, process.Name