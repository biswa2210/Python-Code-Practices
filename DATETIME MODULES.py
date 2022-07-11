import datetime
import time
initial=time.time()
def getdatetime():
    return datetime.datetime.now()

for i in range(60):
  print(getdatetime())
  time.sleep(1)
  print(time.asctime(time.localtime(time.time())))#its used to print localtime
final=time.time()
print(final-initial)