import multiprocessing
import time
def add_up( q, max_counter ):
    counter = 0
    while counter < max_counter:
        counter += 1
        q.put( counter ) #this basically places the counter in the Queue q
        time.sleep(0.5)
if __name__ == "__main__": # Necessary! To start the main process.
    q = multiprocessing.Queue()#this initializes the Queue
    p1 = multiprocessing.Process( target=add_up, args=[q,10] )#initializes the multiprocessing 
    p1.start()# starts it
    p1.join()# ends it
    while not q.empty(): #checks that the Queue build isn't empty
        num = q.get()# This retrieves the value in the Queue
        print( num )
    print( "end" )


    #IDEAS to build
    # Find all prime numbers between 0 and 500