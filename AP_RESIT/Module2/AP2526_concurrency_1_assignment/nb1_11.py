# NB1_11.py

from math import sqrt

def is_prime( n ):
    if n < 2:
        return False
    i = 2
    while i <= sqrt( n ):
        if n % i == 0:
            return False
        i += 1
    return True

### Exercise 5 ###############################


    
##############################################