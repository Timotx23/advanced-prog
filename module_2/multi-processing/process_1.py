import multiprocessing
import time
def add_up( max_counter ):
    counter = 0
    while counter < max_counter:
        counter += 1
        print( counter ) # You do not see this under windows!
        time.sleep(1)
if __name__ == "__main__": # Necessary! To start the main process.
    p1 = multiprocessing.Process( target=add_up, args=[20] )
    p1.start()
    p1.join()
    print( "end" )