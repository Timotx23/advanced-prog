# NB2_13.py

import threading as tr, time, random

### Exercise 11 ##############################
# Context:
# A small repair shop has only a limited number of repair stations.
#
# Many customers arrive at the same time, but only `stations` customers
# may be repaired at once.
#
# Each customer must receive a unique repair ticket number.
#
# Your job is to fill in the RepairShop class.
#
# Requirements:
# - At most `stations` customers may be inside the repair area at once.
# - Every customer must get a unique ticket number.
# - Ticket numbers must be exactly 1, 2, 3, ..., customers.
# - Every customer must call startRepair(ticket) before finishRepair(ticket).
#
# You may edit only the RepairShop class.
# Do not edit the tests.

class RepairShop:
    def __init__( self, stations ):
        # Fill in this method.
        self.stations = stations
        self.sema = tr.Semaphore(stations)
        self.lock = tr.Lock()
        self.ticket = 1
        
        

    def repair( self, startRepair, finishRepair ):
        # Fill in this method.
        
        with self.sema:
            with self.lock:
                ticket = self.ticket
                self.ticket +=1
            startRepair(ticket)
            finishRepair(ticket)
       

##############################################


### Tests ####################################

def run_test( stations, customers ):
    shop = RepairShop( stations )

    active = 0
    max_active = 0
    tickets = []
    completed = []
    check_lock = tr.Lock()

    def startRepair( ticket ):
        nonlocal active, max_active

        with check_lock:
            active += 1
            max_active = max( max_active, active )
            tickets.append( ticket )

            assert active <= stations, f"Too many customers inside: {active}"
            assert ticket not in completed, f"Ticket {ticket} finished before it started"

        time.sleep( random.random()/50 )

    def finishRepair( ticket ):
        nonlocal active

        with check_lock:
            assert ticket in tickets, f"Ticket {ticket} finished without starting"
            completed.append( ticket )
            active -= 1

        time.sleep( random.random()/50 )

    threads = [
        tr.Thread( target=shop.repair, args=(startRepair, finishRepair) )
        for _ in range( customers )
    ]

    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    assert max_active <= stations, f"Expected at most {stations} active repairs, got {max_active}"
    assert sorted( tickets ) == list( range(1, customers+1) ), f"Bad ticket numbers: {tickets}"
    assert sorted( completed ) == list( range(1, customers+1) ), f"Not all repairs completed: {completed}"


if __name__ == "__main__":
    run_test( stations=1, customers=10 )
    run_test( stations=2, customers=25 )
    run_test( stations=3, customers=50 )
    run_test( stations=5, customers=100 )

    print( "All tests passed." )