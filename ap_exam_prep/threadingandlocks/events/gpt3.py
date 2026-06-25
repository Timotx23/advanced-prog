# NB2_11.py

import threading as tr, time, random

### Exercise 9 ###############################
# Context:
# Three threads must print in a strict repeating order:
#
#     red, green, blue, red, green, blue, ...
#
# The threads may start in any order.
# Your job is to fill in the OrderedPrinter class so the output order is always correct.
#
# You may edit only the OrderedPrinter class.
# Do not edit the tests.



class OrderedPrinter:
    def __init__( self, rounds ):
        self.rounds = rounds
       
        self.reds,self.greens,self.blues = [tr.Event() for _ in range(3)]

        # Fill in this method.
        self.reds.set()

      

    def red( self, printRed ):
        # Fill in this method.
        for i in range(self.rounds):
            self.reds.wait()
            
            printRed()
            self.reds.clear()
            self.greens.set()
        
       

    def green( self, printGreen ):
        # Fill in this method.
        for i in range(self.rounds):
            self.greens.wait()
            printGreen()
            self.greens.clear()
            self.blues.set()

       

    def blue( self, printBlue ):
        # Fill in this method.
        for i in range(self.rounds):
            self.blues.wait()
            printBlue()
            self.blues.clear()
            self.reds.set()
        
        

##############################################


### Tests ####################################

def run_test( rounds ):
    output = []
    printer = OrderedPrinter( rounds )

    def printRed():
        output.append( "red" )

    def printGreen():
        output.append( "green" )

    def printBlue():
        output.append( "blue" )

    threads = [
        tr.Thread( target=printer.blue, args=(printBlue,) ),
        tr.Thread( target=printer.green, args=(printGreen,) ),
        tr.Thread( target=printer.red, args=(printRed,) )
    ]

    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    expected = []
    for _ in range( rounds ):
        expected += [ "red", "green", "blue" ]

    assert output == expected, f"Expected {expected}, but got {output}"


if __name__ == "__main__":
    for rounds in [1, 2, 5, 10, 25]:
        run_test( rounds )

    print( "All tests passed." )