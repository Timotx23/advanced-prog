# NB2_04.py

import threading, time

### Exercise 3 ###############################

def playTennis( num ):  
    print( f"Player {num} is playing" )
    time.sleep(1) 
    print( f"Player {num} is leaving the table" )

##############################################
    
players = []
for x in range(16):
    players += [threading.Thread( target=playTennis, args=(x,) )]
for player in players:
    player.start()
for player in players:
    player.join()
print( "end" )
    
