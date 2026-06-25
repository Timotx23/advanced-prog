# NB2_09.py

import threading as tr, time, random

COUNT = 5
ROUNDS = 10
balance = 0
lock = tr.Lock()

### Exercise 7 ###############################

def worker( num ):
    global balance
  
    for i in range( ROUNDS ):
        print( f"Worker {num} is preparing..." )
        time.sleep( random.random()/10 )
        with lock:
            current = balance
            print( f"Worker {num} reads balance: {current}" )
            time.sleep( random.random()/20 )
            balance = current + 1
            print( f"Worker {num} writes balance: {balance}" )
    
    print( f"Worker {num} says: \"Done!\"" )
    
##############################################    
    
if __name__ == "__main__":
    threads = [ tr.Thread( target=worker, name=f'T{name}', args=(name,)) for name in range(COUNT) ]
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
    print( f"Final balance should be {COUNT * ROUNDS}" )
    print( f"Final balance is {balance}" )