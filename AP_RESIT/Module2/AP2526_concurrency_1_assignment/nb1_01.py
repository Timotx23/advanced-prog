# NB1_01.py

import threading
import time

def sayMessage( message, reps ): 
    for _ in range( reps ):      # `_` is commonly used as a throwaway variable, a placeholder in loops
        print( message )
        time.sleep(1)

t1 = threading.Thread( target=sayMessage, args = ("Hello, world!", 10) )
t1.start() 
print('We can run other instructions while the thread is alive.')
time.sleep(3) #pause the main program
print('The thread keeps running while the main program sleeps.')
t1.join() 
print('end')