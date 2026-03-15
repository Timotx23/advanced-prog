import threading
import time
switch = True
def poll_switch(): # Can only flip twice
    global switch
    while True:
        if input( "Flip switch? (Y/N): " ).lower()[0] == 'y':
            switch = not switch
            if switch:
                return
def add_up( max_counter ):
    counter = 0
    while counter < max_counter:
        if switch:
            counter += 1
    print( counter )
    time.sleep(1)
t1 = threading.Thread( target=add_up, args=[20] )
t2 = threading.Thread( target=poll_switch )
t1.start(); t2.start(); t1.join(); t2.join()
print( "end" )