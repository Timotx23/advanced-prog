# NB2_14.py

import threading as tr, time, random
from queue import Queue

### Exercise 12 ##############################
# Context:
# A factory has several producer threads and several consumer threads.
#
# Producers create numbered parts and put them into a shared queue.
# Consumers take parts from the queue and inspect them.
#
# Your job is to fill in the FactoryLine class.
#
# Requirements:
# - Every produced part must be inspected exactly once.
# - Consumers must stop naturally after all work is done.
# - The program must not hang.
# - The final inspected list may be in any order.
# - You may use Queue, locks, sentinels, or other threading tools.
#
# You may edit only the FactoryLine class.
# Do not edit the tests.
SENTINAL = "end"
class FactoryLine:
    def __init__( self, producers, consumers, parts_per_producer ):
        self.producers = producers
        self.consumers = consumers
        self.parts_per_producer = parts_per_producer
        self.producers_done = 0
  
        self.lock = tr.Lock()
        self.queue = Queue()
        # Fill in this method.
        

    def produce( self, producer_id, createPart ):
        for i in range( self.parts_per_producer ):
            part = createPart( producer_id, i )
            self.queue.put( part )

        with self.lock:
            self.producers_done += 1

            if self.producers_done == self.producers:
                for i in range( self.consumers ):
                    self.queue.put( SENTINAL )
        
        

    def consume( self, inspectPart ):
        # Fill in this method.
        while True:
            getter = self.queue.get()
            if getter == SENTINAL:
                self.queue.task_done()
                break
            inspectPart(getter)
            self.queue.task_done()
    

##############################################


### Tests ####################################

def run_test( producers, consumers, parts_per_producer ):
    line = FactoryLine( producers, consumers, parts_per_producer )

    produced = []
    inspected = []
    check_lock = tr.Lock()

    def createPart( producer_id, part_id ):
        time.sleep( random.random()/100 )
        part = f"P{producer_id}-{part_id}"

        with check_lock:
            produced.append( part )

        return part

    def inspectPart( part ):
        time.sleep( random.random()/100 )

        with check_lock:
            assert part not in inspected, f"Part inspected twice: {part}"
            inspected.append( part )

    producer_threads = [
        tr.Thread( target=line.produce, args=(i, createPart) )
        for i in range( producers )
    ]

    consumer_threads = [
        tr.Thread( target=line.consume, args=(inspectPart,) )
        for _ in range( consumers )
    ]

    threads = producer_threads + consumer_threads
    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in producer_threads:
        t.join( timeout=3 )

    line.queue.join()

    for t in consumer_threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    expected = [
        f"P{producer_id}-{part_id}"
        for producer_id in range( producers )
        for part_id in range( parts_per_producer )
    ]

    assert sorted( produced ) == sorted( expected ), f"Bad produced list: {produced}"
    assert sorted( inspected ) == sorted( expected ), f"Bad inspected list: {inspected}"


if __name__ == "__main__":
    run_test( producers=1, consumers=1, parts_per_producer=10 )
    run_test( producers=2, consumers=3, parts_per_producer=25 )
    run_test( producers=5, consumers=2, parts_per_producer=20 )
    run_test( producers=4, consumers=4, parts_per_producer=50 )

    print( "All tests passed." )