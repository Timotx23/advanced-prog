# NB2_08.py

import threading as tr, time, random

COUNT = 3
ROUNDS = 10
fork = []
for i in range( COUNT ):
    fork.append( tr.Lock() )

### Exercise 6 ###############################

def philosopher( num ):
    first = (num-1)%COUNT
    second = num
    fork1 = "left"
    fork2 = "right"
    first = fork[first]
    second = fork[second]
    for i in range( ROUNDS ):
        print( f"Philosopher {num} is thinking..." )
        time.sleep( random.random() )
        with first:
            print( f"Philosopher {num} takes {fork1} fork." )
            time.sleep( random.random()/3 )
            with second:
                print( f"Philosopher {num} takes {fork2} fork." )
                print( f"Philosopher {num} is eating..." )
                time.sleep( random.random() )
                print( f"Philosopher {num} puts down {fork2} fork." )
            print( f"Philosopher {num} puts down {fork1} fork." )
    print( f"Philosopher {num} says: \"Eureka!\"" )
    
##############################################    
    
if __name__ == "__main__":
    threads = [ tr.Thread( target=philosopher, name=f'T{name}', args=(name,)) for name in range(COUNT) ]
    for t in threads:
        t.start()