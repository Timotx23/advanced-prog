# NB2_10.py

import threading as tr, time, random, queue

COUNT = 4
JOBS = 12

tasks = queue.Queue()

for i in range( JOBS ):
    tasks.put( i )

### Exercise 8 ###############################
lock = tr.Lock()
def worker( num ):
    with lock:
        while not tasks.empty():
            print( f"Worker {num} is looking for a task..." )
            time.sleep( random.random()/10 )
            
            task = tasks.get()
            print( f"Worker {num} got task {task}." )
            
            time.sleep( random.random()/5 )
            print( f"Worker {num} finished task {task}." )
            
            tasks.task_done()
    
    print( f"Worker {num} says: \"No more work!\"" )
    
##############################################    
    
if __name__ == "__main__":
    threads = [ tr.Thread( target=worker, name=f'T{name}', args=(name,)) for name in range(COUNT) ]
    for t in threads:
        t.start()
        
    tasks.join()
        
    for t in threads:
        t.join()
        
    print( "All tasks are done." )