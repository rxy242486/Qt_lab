import threading
import sys
import time
def hello(id,times):
    for i in range(times):
        print "hello %s time is %d\n" % (id,i)
        #time.sleep(5)
if __name__ == "__main__":
    t = threading.Thread(target=hello,args=("hawk",5))
    t.start()
