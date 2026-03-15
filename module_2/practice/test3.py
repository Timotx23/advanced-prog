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

def calling_prime(last_known,i):
    
    if is_prime(i) and i> last_known:
        last_known=i+1
        while not is_prime(last_known):
            last_known+=1
        return last_known
    else:
        return f"{i} Was not larger than last known or was not a prime"
    
for b in range(5):
    last_known=2
    num = int( input( "Give me a bigger prime number bigger than "+str( last_known )+": " ) )
    call_prime=calling_prime(last_known, num)
    if type(call_prime) == int:
        last_known = call_prime
        print( last_known, "is prime and bigger than", num ) #prints out the value found
    else:
        print(call_prime)
        break

