#Python wmi Cookbook#
import wmi
import time,os,datetime
import win32api
import win32con

c=wmi.WMI()

print "process list-------------------------"
for process in c.Win32_Process():
  print process.ProcessId, process.Name
  
print "create notepad-------------------------"
process_id, return_value = c.Win32_Process.Create(CommandLine="notepad.exe")
for process in c.Win32_Process (ProcessId=process_id):
  print process.ProcessId, process.Name

result = process.Terminate()

#show parameter
print c.Win32_Process.Create

print "pid list-------------------------"
for process in c.Win32_Process(name="notepad.exe"):
  print process.ProcessId, process.Name

print "server not in normal status-------------------------"
stopped_services = c.Win32_Service(StartMode="Auto", State="Stopped")
if stopped_services:
  for s in stopped_services:
    print s.Caption, "service is not running"
else:
  print "No auto services stopped"
  
print "disk caption-------------------------"
for disk in c.Win32_LogicalDisk(DriveType=3):
  print disk.Caption, "%0.2f%% free" %(100.0 * long(disk.FreeSpace) / long(disk.Size))

print "physical_disk-------------------------"
  
for physical_disk in c.Win32_DiskDrive():
  for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
    for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
      print physical_disk.Caption, partition.Caption, logical_disk.Caption
      
print "disk TYPES-------------------------"
DRIVE_TYPES = {
  0 : "Unknown",
  1 : "No Root Directory",
  2 : "Removable Disk",
  3 : "Local Disk",
  4 : "Network Drive",
  5 : "Compact Disc",
  6 : "RAM Disk"
}


for drive in c.Win32_LogicalDisk():
  print drive.Caption, DRIVE_TYPES[drive.DriveType]
  
print "open file,wait input,show input -------------------------"
filename = r"e:\temp.txt"
process = c.Win32_Process
process_id, result = process.Create(CommandLine="notepad.exe " + filename)
watcher = c.watch_for(
  notification_type="Deletion",
  wmi_class="Win32_Process",
  delay_secs=1,
  ProcessId=process_id
)
 
watcher()
print "This is what you wrote:"
print open(filename).read()


print "watch print job-------------------------"

# print_job_watcher = c.Win32_PrintJob.watch_for(
#   notification_type="Creation",
#   delay_secs=1
# )
#  
# while 1:
#   pj = print_job_watcher()
#   print "User %s has submitted %d pages to printer %s" % \
#     (pj.Owner, pj.TotalPages, pj.Name)
    
print "show ip mac address-------------------------"

for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
  print interface.Description, interface.MACAddress
  for ip_address in interface.IPAddress:
    print ip_address
  print
  


print "show startup server-------------------------"

for s in c.Win32_StartupCommand():
  print "[%s] %s <%s>" %(s.Location, s.Caption, s.Command)
  
  
print "watch error log-------------------------"
# watcher = c.watch_for(
#   notification_type="Creation",
#   wmi_class="Win32_NTLogEvent",
#   Type="error"
# )
# while 1:
#   error = watcher()
#   print "Error in %s log: %s" %(error.Logfile, error.Message)
  # send mail to sysadmin etc.
  

  
print "show share director-------------------------"
for share in c.Win32_Share():
  print share.Name, share.Path


print "show print job-------------------------"
for printer in c.Win32_Printer():
  print printer.Caption
  for job in c.Win32_PrintJob(DriverName=printer.DriverName):
    print "  ", job.Document
  print

print "software install tip:you hava a right to install-------------------------"
c.Win32_Product.Install(
  PackageLocation="E:/Download/mysql-utilities-1.5.6-winx64.msi",
  AllUsers=False
)

print "show signature-------------------------"
for opsys in c.Win32_OperatingSystem ():
  break
 
print opsys.Reboot
print opsys.Shutdown

for line in os.popen("at"):
  print line

print "create ScheduledJob-------------------------"
one_minutes_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
job_id, result = c.Win32_ScheduledJob.Create(
  Command=r"cmd.exe /c dir /b c:\ > c:\\temp.txt",
  StartTime=wmi.from_time(one_minutes_time)
)
print job_id

print "create MINIMIZED Process-------------------------"
SW_SHOWMINIMIZED = 1

startup = c.Win32_ProcessStartup.new(ShowWindow=SW_SHOWMINIMIZED)
pid, result = c.Win32_Process.Create(
  CommandLine="notepad.exe",
  ProcessStartupInformation=startup
)
print pid

print "create namespaces-------------------------"

def enumerate_namespaces(namespace=u"root", level=0):
  print level * "  ", namespace.split("/")[-1]
  c = wmi.WMI(namespace=namespace)
  for subnamespace in c.__NAMESPACE():
    enumerate_namespaces (namespace + "/" + subnamespace.Name, level + 1)
 
enumerate_namespaces()

print "desktop.Wallpaper-------------------------"
full_username = win32api.GetUserNameEx(win32con.NameSamCompatible)
for desktop in c.Win32_Desktop(Name=full_username):
  print \
    desktop.Wallpaper or "[No Wallpaper]", \
    desktop.WallpaperStretched, desktop.WallpaperTiled