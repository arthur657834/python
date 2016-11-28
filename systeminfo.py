import psutil
mem = psutil.virtual_memory()
print mem
print mem.total,mem.used,mem.free

print psutil.swap_memory()

cpu = psutil.cpu_times()
print cpu

print psutil.cpu_count()
print psutil.cpu_count(logical=False)

print psutil.disk_partitions()
print psutil.disk_usage('/')
print psutil.disk_io_counters()
print psutil.disk_io_counters(perdisk=True)

print psutil.net_io_counters()

print psutil.users()
print psutil.boot_time()

print psutil.pids()
x=psutil.Process(15421)
#see the ide tips
print x.name() 

from subprocess import PIPE
proc = psutil.Popen(["python","-c","print('hello')"],stdout=PIPE)
print proc.name()


