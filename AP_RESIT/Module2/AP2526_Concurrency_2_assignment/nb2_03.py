# NB2_03.py

### Exercise 2 ###############################

from time import sleep
from random import random
from threading import *

def report( lock, identifier ):
    with lock:
        sleep(1)
        print( f"Process {identifier} reported" )

def task( lock, identifier, value ):
    with lock:
        print( f"Process {identifier} running... " )
        sleep(value)
        report( lock, identifier )

def main():
    lock = Lock()
    threads = [Thread( target=task, args=(lock, i, random()) ) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

##############################################
