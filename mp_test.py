import time
from multiprocessing import Process, Queue, Pipe

#For string s of length sn, calculate the time of exhanging objects between processors.
#Find the mean time of n processors.

sn=10 #String length
n=10 #Total processors

s = ""
mean=0
for i in range(sn):
    s=s+'a'
ps = []

##### Using queue.

q = Queue()
    
def f(a):
    a.put(s)

for i in range(n): 
    ps.append(Process(target=f, args=(q,)))

for p in ps:
    p.start()
    t1=time.time()
    res=q.get()
    t2=time.time()
    mean+= t2-t1

print "Queue time: " + (str)(mean/(n))

for p in ps:
    p.join

##### Using pipe.
mean=0

parent_conn, child_conn = Pipe()

def fu(conn):
    conn.send(s)
    conn.close()

for i in range(n): 
    ps.append(Process(target=fu, args=(child_conn,)))

for p in ps:
    p.start()
    t1=time.time()
    res= parent_conn.recv()  
    t2=time.time()
    mean+= t2-t1

print "Pipe time: " + (str)(mean/(n))

for p in ps:
    p.join
    
