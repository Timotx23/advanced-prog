import threading
import time
class MessageThread( threading.Thread ):
    def __init__( self, message, count ):
        self.message = message
        self.count = count
        super().__init__() # create the thread
    def run( self ): # override run() from Thread
        for _ in range( self.count ):
            time.sleep( 1/self.count )
            print( self.message )
t1 = MessageThread( "Hello, world!", 10 )
t2 = MessageThread( "How are you today?", 5 )
t1.start()
t2.start()
t1.join()
t2.join()
print( "end" )