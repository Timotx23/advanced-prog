import threading
import time
counter = 0
def add_up( max_add ):
    global counter
    for _ in range( max_add ):
        c = counter + 1 #they share a counter meaning one adds then the other etc so it all continous like this
        time.sleep(1/max_add)# This allows that interwieving effect pausing one thread it allows the other to catch
        counter = c
        print( counter )
t1 = threading.Thread( target=add_up, args=[5] )
t2 = threading.Thread( target=add_up, args=[10] )
t1.start()
t1.join()
t2.start()

t2.join()
print( "end" )