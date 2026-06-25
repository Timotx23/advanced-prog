# NB2_05.py

import threading, time

### Exercise 4 ###############################

def subtask( i ):
    print( f"Thread {i} started..." )
    # ...the subtask can do anything here, and then wait for a signal to continue
    print( "Waiting for the signal..." )
    # ...should receive a signal
    print( "Signal received!" )
    # ...the thread can now use the shared resource
    print( f"Thread {i} continues..." )
    print( f"Thread {i} was completed" )

def task( nsubtasks=3 ):
    pool=[]
    for i in range( nsubtasks ):
        pool.append( threading.Thread( target=subtask, args=(i,)) )
    for i in range( nsubtasks ):
        pool[i].start()
    print( 'The main task is running now...' )
    time.sleep(3) 
    print( 'The main task is finished. Sending a signal for subtasks to proceed...' )
    for i in range( nsubtasks ):
        pool[i].join()

##############################################
    
if __name__ == "__main__":
    task( nsubtasks=4 )

