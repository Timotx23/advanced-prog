import threading, time
from queue import Queue
#EXAMPLE of concurrent design meaning everything is moving together 
SENTINEL="END"

def turn_to_list(x):
    lst2=[x]
    [lst2.append(j) for j in range(1,x) if x%j ==0]
    return lst2

def is_prime(value):
    if value <=1:
        return False
    return len(turn_to_list(value))<=2 
#this is the only really new part of the threading  
def put_in_queue(in_q: Queue, out_q: Queue):
    """This function should put something into the queue
    This is also called the producer
    """
    while True:
        n=in_q.get()
        if n == SENTINEL:
            in_q.task_done()
            out_q.put(SENTINEL)
            break
        
        if is_prime(n):      # now boolean
            out_q.put(n)
        in_q.task_done()
    
def get_from_queue(out_q: Queue):
    """This is typically called the consumer as it gets things from the queue"""
    while True:
        item = out_q.get()
        if item == SENTINEL:
            out_q.task_done()
            break

        print(item)
        out_q.task_done()

N = 50
q1 = Queue()
q2 = Queue()

t1 = threading.Thread(target=put_in_queue, args=(q1, q2))
t2 = threading.Thread(target=get_from_queue, args=(q2,))

t1.start()
t2.start()

# Producer: push work into q1
for n in range(N + 1):
    q1.put(n)

# Tell worker to stop after finishing all numbers
q1.put(SENTINEL)

# Wait until all queued work is fully processed
q1.join()
q2.join()

t1.join()
t2.join()
print("end")


