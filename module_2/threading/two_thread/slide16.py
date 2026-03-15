import threading
import time
def add_up( max_counter ):
    """This function has multi threading where 2 threads wourk at the same time
    if you try to stop it u must stop it 2x as there are 2 threads
    """
    counter = 0
    while counter < max_counter:
        counter += 1
        print( counter )
        time.sleep(1)  #target is the function being threaded, args= the number of itterations
t1 = threading.Thread( target=add_up, args=[20] )#This is the sysntax to create threads
t1.start()# Starts the threading
t1.join() #ends the threading by joining the threads back together
print( "end" )