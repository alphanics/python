# Python Thread

```python
def yourFunc():
    print "Funcion called!!"
thread.start_new_thread(yourFunc, ())
```

```python 
import time
from threading import Thread

def myfunc(i):
    print ("Before Sleep :", i)
    time.sleep(5)
    print ("After Sleep :", i)
    
for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
```    


## thread class
```python
 
import threading
import datetime

class MyThreadClass(threading.Thread):
  def run(self):
    dt = datetime.datetime.now()
    print (self.getName(), " Current Date and Time : ",  dt)
    
for i in range(5):
  t = MyThreadClass()
  t.start()
```
