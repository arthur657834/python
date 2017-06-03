import _winreg
import wmi

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")

try:
    i = 0
    while 1:
         name, value, type = _winreg.EnumValue(key, i)
         print repr(name),
         i +=1
except WindowsError:
    print
    
print "-------------------"

value, type = _winreg.QueryValueEx(key, "ExplorerStartupTraceRecorded")
print value, type 

print _winreg.REG_SZ

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")

newKey = _winreg.CreateKey(key,"MyNewkey")
 
_winreg.SetValue(newKey,"ValueName",_winreg.REG_SZ,"ValueContent")

#delete not work
_winreg.DeleteKey(key, "MyNewkey")

_winreg.DeleteValue(key, "ValueName")

#remore
key = _winreg.ConnectRegisty("IP地址或者机器名",_winreg.HKEY_CURRENT_USER)