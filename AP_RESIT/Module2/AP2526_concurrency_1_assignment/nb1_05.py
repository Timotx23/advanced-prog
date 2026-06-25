# NB1_05.py

import threading, time

greeting = 'Hi'

def greet_once(): 
    global greeting
    print( greeting )
    time.sleep(2)
    greeting = ''
    print( 'other stuff that this function does' )

threads = []

for _ in range(10):
    threads.append( threading.Thread( target=greet_once ) )
for t in threads:
    t.start()
for t in threads:
    t.join()

print( "end" )