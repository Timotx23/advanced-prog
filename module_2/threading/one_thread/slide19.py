import time
switch = True
def poll_switch():
    global switch
    if input( "Flip switch? (Y/N): " ).lower()[0] == 'y':
        switch = not switch
def add_up( max_counter ):
    counter = 0
    while counter < max_counter:
        poll_switch()
        if switch:
            counter += 1
    print( counter )
    time.sleep(1)
add_up( 20 )