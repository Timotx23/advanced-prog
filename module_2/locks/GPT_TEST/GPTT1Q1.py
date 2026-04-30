# NB1_07.py


import multiprocessing, time


SENTINEL = "END"

def producer( q, n ):
    for a in range( n+1 ):
        q.put(a)
    q.put( SENTINEL ); q.put( SENTINEL )
    
def consumer( q1, q2 ):
    while True:
        num = q1.get()
        time.sleep(0.1)
   
        if num == SENTINEL:
            break
        q2.put( num )

if __name__ == "__main__":

    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    prd = multiprocessing.Process( target=producer, args=(q1,25) )
    cns1 = multiprocessing.Process( target=consumer, args=(q1,q2) )
    cns2 = multiprocessing.Process( target=consumer, args=(q1,q2) )
    cns3 = multiprocessing.Process( target=consumer, args=(q1,q2) )
    

    prd.start() , cns1.start(), cns2. start()
    cns1.join(), cns2.join(), prd.join()

    while not q2.empty():
        num = q2.get()
    
        print( num )


   
    print('end')
