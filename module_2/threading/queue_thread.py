import threading, time
from queue import Queue
SENTINEL = "END"
def producer( q, n ):
    for a in range( n+1 ):
        q.put(a)
    q.put( SENTINEL ); q.put( SENTINEL )
def consumer( q1, q2 ):
    while True:
        num = q1.get()
        time.sleep(0.1)
        q1.task_done()
        if num == SENTINEL:
            break
        q2.put( num )
q1 = Queue(); q2 = Queue()
cns1 = threading.Thread( target=consumer, args=(q1,q2) )
cns2 = threading.Thread( target=consumer, args=(q1,q2) )
prd = threading.Thread( target=producer, args=(q1,25) )

cns1.start(); cns2.start(); prd.start()
q1.join(); cns1.join(); cns2.join(); prd.join()

while not q2.empty():
    num = q2.get()
    q2.task_done()
    print( num )
q2.join() 