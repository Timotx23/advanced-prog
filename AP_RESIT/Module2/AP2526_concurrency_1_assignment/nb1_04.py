# NB1_04.py

import threading
from math import sqrt

def is_prime( n ):
    if n < 2:
        return False
    i = 2
    while i < sqrt( n )+1:
        if n % i == 0:
            return False
        i += 1
    return True

### Exercise 2 ###############################



##############################################

numbers = [1000000007,1000000011,980835832582657,980835832582653,999998727899999,
           1000000411,1008495923,1056689261,2147483647,2147483643]
threads = []

for n in numbers:
    threads.append( PrimeThread( n ) )
for t in threads:
    t.start()
for t in threads:
    t.join()

print('end')