# NB1_03.py

import threading
import time

def sayMessage( message, reps ): 
    for _ in range( reps ):      # `_` is commonly used as a throwaway variable, a placeholder in loops
        print( message )
        time.sleep(1)

dry_fruits=['achene', 'capsule', 'caryopsis', 'cypsela', 'fibrous drupe', 'follicle',
    'legume', 'loment', 'nut', 'samara', 'schizocarp', 'silique', 'silicle', 'utricle' ]

threads = []

### Exercise 1 ###############################



##############################################

print( 'End of program.' )