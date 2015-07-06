# python_threading_multiprocessing_timeTests

I have tested the times of some jobs by using multiprocessing and threading in Python. 

*** Threading ***

Threads allow working with more than one thread or job. "Threading" is a higher level interface for threads. 
Two threads exchange information between each other by the "event" objects. "set" method puts a flag for the event and "wait" method waits for a flag to get set.  

In the "thr_test.py" test code, there are two threads and their job is to increment the counter, "cnt", until it is equal to "COUNTER"*2.  
First event is correlated with the first thread and function, "f". The second event is correlated with the second thread and function, "g".
The jobs are repeated "n" times. 


*** MultiProcessing ***

Because of the Global Interpreter Lock in CPython, only one thread can execute one Python code at once. To overcome this limitation, you can use multiprocessing which allows to work in different cores simultaneously. Therefore, multiprocessing has a similar duty with threading but in a different way. 

Exchanging objects between different processes can be done by using a queue or a pipe. Queue has one end, it has "put()" and "get()" methods. Pipe has two ends and has "send()" and "receive()" methods, the elements that are sent to one end should be received from the other end, otherwise it will cause a corruption. 

In the "mp_test.py" code, two seperate jobs are defined in different methods. The first job is to put a string to a queue and get it. Time is measured before and after using "get" method and the difference is found. The second job is to send a string to a pipe and receive it. Time is measured for "recv()" method. "n" holds the number of processes and "sn" holds the length of the string that will be used while communicating.


*** Results ***

The test codes are executed for different values. The related graphs and the results are in the pdf document. In general, it can be seen that threading is more faster than multiprocessing. In multiprocessing, usage of pipes is faster than queues. 



More info: 
1. https://docs.python.org/2/library/threading.html#threading.Event.set
2. https://docs.python.org/2/library/multiprocessing.html
