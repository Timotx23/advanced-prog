# NB2_07.py

import threading, time

fork = threading.Lock()
knife = threading.Lock()

### Exercise 5 ###############################

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

##############################################

print( "start" )
t1 = threading.Thread( target=eating1 )
t2 = threading.Thread( target=eating2 )
t1.start()
t2.start()
t1.join()
t2.join()
print( "end" )