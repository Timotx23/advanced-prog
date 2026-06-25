# NB2_02.py

import threading, time

numlist = list( range(10) )
total = 0

### Exercise 1 ###############################

def process():
    global total
    global numlist
    while True:
        if len( numlist ) <= 0:
            return
        total += numlist[0]
        time.sleep(0.1)
        del numlist[0]

##############################################

tr1 = threading.Thread( target=process, args=[] )
tr2 = threading.Thread( target=process, args=[] )
tr1.start()
tr2.start()
tr1.join()
tr2.join()
print( total )
print( 'end' )