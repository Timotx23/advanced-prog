import threading
import time
class SquareThread( threading.Thread ): #the class inherits the thread class -> this allows in future to open a new thread
    def __init__( self, number ):
        super().__init__() # create the thread 
        self.number = number
        self.return_value = -1
    def run( self ): # override run() from Thread
        time.sleep( 1 )
        self.return_value = self.number*self.number
t1 = SquareThread( 15 )
t2 = SquareThread( 24 )
t1.start(); t2.start(); t1.join(); t2.join() # this actually executes the thread
print( f"The square of {t1.number} is {t1.return_value}" )
print( f"The square of {t2.number} is {t2.return_value}" )