import time
import threading 

#Test the time between wait and set methods between two events in threading.

COUNTER=10 # Number of jobs(in this code, a job is incrementing the variable cnt until COUNTER)
n=10 # Number of job performs (helps to calculate an average value of times)

print "Average time of performing "+ (str)(COUNTER)+ " jobs "+ (str)(n) + " times:"

event=threading.Event()
event2=threading.Event()

def f():
	global cnt
	while(cnt<COUNTER*2):
		event.wait()
		cnt=cnt+1
		event2.set()
    
def g():
	global cnt
	while(cnt<COUNTER*2):
		cnt=cnt+1
		event.set()
		event2.wait()

mean=0

for i in range(n):
	cnt=0
	thr= threading.Thread(target=f)
	thr2= threading.Thread(target=g)
	thr.start()
	thr2.start()
	t1=time.time()
	thr.join()
	thr2.join()
	t2=time.time()
	mean = mean+ t2-t1

print mean/n

