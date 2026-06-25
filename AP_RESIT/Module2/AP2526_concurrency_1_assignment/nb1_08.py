# NB1_08.py

import multiprocessing
import time

def sayMessage( message, reps ): 
    for _ in range( reps ):      # `_` is commonly used as a throwaway variable, a placeholder in loops
        print( message )
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process( target=sayMessage, args = ("Hello, world!", 10) )
    p1.start() 
    print('We can run other instructions while the process is alive.')
    time.sleep(3) #pause the main program
    print('The process keeps running while the main program sleeps.')
    p1.join() 
    print('end')
