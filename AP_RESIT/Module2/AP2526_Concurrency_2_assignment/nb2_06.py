# NB2_06.py

#WARNING: Since this example recreates a deadlock, 
#you will have to interrupt the execution.

import threading, time

fork = threading.Lock()
knife = threading.Lock()

def eating1():
    with knife:
        time.sleep(3)
        with fork:
            print( "Much Munch Munch" )
            
def eating2():
    with fork:
        time.sleep(3)
        with knife: 
            print( "Chomp Chomp Chomp" )
            
print( "start" )
t1 = threading.Thread( target=eating1 )
t2 = threading.Thread( target=eating2 )
t1.start()
t2.start()
t1.join()
t2.join()
print( "end" )