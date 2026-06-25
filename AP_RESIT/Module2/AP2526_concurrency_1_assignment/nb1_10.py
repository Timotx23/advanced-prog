# NB1_10.py

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

print( "2 is the lowest prime number" )
lastnum = 2
while True:
    num = int( input( "Give me a bigger prime number bigger than "+str( lastnum )+": " ) )
    if num <= lastnum:
        print( "That number is smaller than", lastnum )
        continue
    if not is_prime( num ):
        print( num, "is not prime. Goodbye!" )
        break
    lastnum = num+1
    while not is_prime( lastnum ):
        lastnum += 1
    print( lastnum, "is prime and bigger than", num )