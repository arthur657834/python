import _winreg
# not work
key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"Software\Microsoft\Windows")
newKey = _winreg.CreateKey(key,"MyNewkey")
'''
上面的代码的执行不会像预想那样创建如下的键:

"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows"

而是会创建如下的键：

"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows"
'''