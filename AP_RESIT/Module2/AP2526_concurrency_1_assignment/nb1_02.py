# NB1_02.py

import threading
import time

def sayMessage( message, reps ): 
    for _ in range( reps ):      # `_` is commonly used as a throwaway variable, a placeholder in loops
        print( message )
        time.sleep(1)
        
t1 = threading.Thread( target=sayMessage, args=("Hello, world!", 10) ) 
t2 = threading.Thread( target=sayMessage, args = ("How are you today?", 5) ) 

t1.start() 
t2.start() 
t1.join() 
t2.join() 

print( "end" )