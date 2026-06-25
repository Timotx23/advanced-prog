# NB2_12.py

import threading as tr, time, random

### Exercise 10 ##############################
# Context:
# Two machines work together to package orders.
#
# Machine A must prepare an item.
# Machine B must seal that same item.
#
# The output must always be:
#
#     prepare 0
#     seal 0
#     prepare 1
#     seal 1
#     prepare 2
#     seal 2
#     ...
#
# The threads may start in any order.
# Your job is to fill in the Packager class so the output order is always correct.
#
# You may edit only the Packager class.
# Do not edit the tests.

class Packager:
    def __init__( self, orders ):
        self.orders = orders
        self.prep, self.seals = [tr.Event() for i in range(2)]
        # Fill in this method.
        self.prep.set()
        pass

    def prepare( self, prepareItem ):
        # Fill in this method.
        for i in range(orders):
            self.prep.wait()
            prepareItem(i)
            self.prep.clear()
            self.seals.set()
      

    def seal( self, sealItem ):
        # Fill in this method.
        for i in range(orders):
            self.seals.wait()
            sealItem(i)
            self.seals.clear()
            self.prep.set()
        

##############################################


### Tests ####################################

def run_test( orders ):
    output = []
    packager = Packager( orders )

    def prepareItem( i ):
        time.sleep( random.random()/100 )
        output.append( f"prepare {i}" )

    def sealItem( i ):
        time.sleep( random.random()/100 )
        output.append( f"seal {i}" )

    threads = [
        tr.Thread( target=packager.seal, args=(sealItem,) ),
        tr.Thread( target=packager.prepare, args=(prepareItem,) )
    ]

    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    expected = []
    for i in range( orders ):
        expected.append( f"prepare {i}" )
        expected.append( f"seal {i}" )

    assert output == expected, f"Expected {expected}, but got {output}"


if __name__ == "__main__":
    for orders in [1, 2, 5, 10, 25, 50]:
        run_test( orders )

    print( "All tests passed." )