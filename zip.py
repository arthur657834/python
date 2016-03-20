import zipfile,os

zfile = zipfile.ZipFile('C:\\Users\\lj\\Desktop\\tmp\\cloudone-all-1.0.0.M1-SNAPSHOT.zip','r')
for filename in zfile.namelist():
    print (filename)
    zfile.extract(filename,'C:\\Users\\lj\\Desktop\\tmp\\')

f = zipfile.ZipFile('e:\\archive.zip','w',zipfile.ZIP_DEFLATED)
os.getcwd()
os.chdir('C:\Users\lj\Desktop\mail-tmp')
f.write('jeecms install.txt')
f.write('wordpress install.txt')
f.close()
