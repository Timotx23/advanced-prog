import time
def add_up( max_counter ):
    """This function just uses 1 thread to execute the task file two_threads/slide16.py does the same task but with 2 threads instead"""
    counter = 0
    while counter < max_counter:
        counter += 1
        print( counter )
        time.sleep(1)
add_up( 20 )