import time
from multiprocessing import Process, Queue, Pipe

#For string s of length sn, calculate the time of exhanging objects between processors.
#Find the average time of n processes.

sn=10 #String length
n=10 #Number of processes

print "Average time of getting a string of length "+ (str)(sn) + " by "+ (str)(n) + " processes"

s = ""
mean=0
for i in range(sn):
    s=s+'a'
ps1 = []
ps2 = []

##### Using queue.

q = Queue()
    
def f(a):
    a.put(s)

for i in range(n): 
    ps1.append(Process(target=f, args=(q,)))

for p in ps1:
    p.start()
    t1=time.time()
    res=q.get()
    t2=time.time()
    mean+= t2-t1

print "Queue: " + (str)(mean/(n)) 

for p in ps1:
    p.join

##### Using pipe.
mean=0

parent_conn, child_conn = Pipe()

def fu(conn):
    conn.send(s)
    conn.close()

for i in range(n): 
    ps2.append(Process(target=fu, args=(child_conn,)))

for p in ps2:
    p.start()
    t1=time.time()
    res= parent_conn.recv()  
    t2=time.time()
    mean+= t2-t1

print "Pipe: " + (str)(mean/(n))

for p in ps2:
    p.join
    
