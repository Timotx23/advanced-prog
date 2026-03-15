import multiprocessing
#this
from math import sqrt
def is_prime( n ):
    if n < 2:
        return (n, False)
    i = 2
    while i <= sqrt( n ):
        if n % i == 0:
            return (n, False)
        i += 1
    return (n, True)
if __name__ == "__main__":
    pool = multiprocessing.Pool( processes=5 )
    # This creates 500 processes; result is a list
    # of all the processes, in the given order:
    result = pool.map( is_prime, range(500) )
    pool.close()
    for n in result:
        if n[1]:
            print( n[0] )
    print('end')