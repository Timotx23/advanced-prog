# NB2_15.py

import threading as tr, time, random
from queue import Queue

### Exercise 13 ##############################
# Context:
# A restaurant has several chefs and one waiter.
#
# Each chef prepares dishes and puts them on the counter.
# The waiter takes dishes from the counter and serves them.
#
# However, dishes from the same chef must be served in order:
#
#     C0-D0 must be served before C0-D1
#     C0-D1 must be served before C0-D2
#     etc.
#
# Dishes from different chefs may be served in any order.
#
# Your job is to fill in the Restaurant class.
#
# Requirements:
# - Every dish prepared by every chef must be served exactly once.
# - Dishes from the same chef must be served in increasing dish number order.
# - Dishes from different chefs may be mixed in any order.
# - The waiter must stop naturally after all dishes are served.
# - The program must not hang.
#
# You may edit only the Restaurant class.
# Do not edit the tests.
SENTINAL = "end"
class Restaurant:
    def __init__( self, chefs, dishes_per_chef ):
        self.chefs = chefs
        self.dishes_per_chef = dishes_per_chef
        self.counter = Queue()
        self.lock = tr.Lock()
        
        self.cheff_count = 0
        
        
        

    def chef( self, chef_id, prepareDish ):
        # Fill in this method.
        for i in range(self.dishes_per_chef):
            self.counter.put(prepareDish(chef_id, i))
           
        with self.lock:
            self.cheff_count +=1
            if self.cheff_count == self.chefs:
                self.counter.put(SENTINAL)
                
    

    def waiter( self, serveDish ):
        # Fill in this method.
        while True:
            getter = self.counter.get()
            if getter == SENTINAL:
                self.counter.task_done()
                break
            serveDish(getter)
            self.counter.task_done()
       

##############################################


### Tests ####################################

def run_test( chefs, dishes_per_chef ):
    restaurant = Restaurant( chefs, dishes_per_chef )

    prepared = []
    served = []
    check_lock = tr.Lock()

    def prepareDish( chef_id, dish_id ):
        time.sleep( random.random()/100 )
        dish = (chef_id, dish_id)

        with check_lock:
            prepared.append( dish )

        return dish

    def serveDish( dish ):
        time.sleep( random.random()/100 )

        with check_lock:
            assert dish not in served, f"Dish served twice: {dish}"
            served.append( dish )

            chef_id, dish_id = dish
            previous = (chef_id, dish_id - 1)

            if dish_id > 0:
                assert previous in served, f"{dish} was served before {previous}"

    chef_threads = [
        tr.Thread( target=restaurant.chef, args=(i, prepareDish) )
        for i in range( chefs )
    ]

    waiter_thread = tr.Thread( target=restaurant.waiter, args=(serveDish,) )

    threads = chef_threads + [waiter_thread]
    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in chef_threads:
        t.join( timeout=3 )

    restaurant.counter.join()

    waiter_thread.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    expected = [
        (chef_id, dish_id)
        for chef_id in range( chefs )
        for dish_id in range( dishes_per_chef )
    ]

    assert sorted( prepared ) == sorted( expected ), f"Bad prepared list: {prepared}"
    assert sorted( served ) == sorted( expected ), f"Bad served list: {served}"


if __name__ == "__main__":
    run_test( chefs=1, dishes_per_chef=10 )
    run_test( chefs=2, dishes_per_chef=15 )
    run_test( chefs=4, dishes_per_chef=20 )
    run_test( chefs=6, dishes_per_chef=25 )

    print( "All tests passed." )