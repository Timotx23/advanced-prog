# Solution with mutex

import threading, time

lock = threading.Lock()
counter = 0

def add_up( max_add ):
    global counter
    for _ in range( max_add ):
        with lock:
            c = counter + 1
            time.sleep(1/max_add)
            counter = c
            print( counter )

t1 = threading.Thread( target=add_up, args=[5] ) 
t2 = threading.Thread( target=add_up, args=[10] ) 
t1.start()
t2.start()
t1.join()
t2.join()
print( "end" )