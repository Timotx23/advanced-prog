# NB2_16.py

import threading as tr, time, random
from queue import Queue

### Exercise 14 ##############################
# Context:
# A logging system has several worker threads and one logger thread.
#
# Worker threads create log messages and put them into a shared queue.
# The logger thread is not allowed to start printing logs immediately.
#
# First, all workers must signal that they are ready.
# Then the logger may begin processing messages from the queue.
#
# Your job is to fill in the LogSystem class.
#
# Requirements:
# - Every worker must call workerReady(worker_id) exactly once.
# - No log may be written before all workers are ready.
# - Every produced log message must be written exactly once.
# - The logger must stop naturally after all logs are written.
# - The program must not hang.
#
# You may use Queue, Event, locks, sentinels, or other threading tools.
#
# You may edit only the LogSystem class.
# Do not edit the tests.

SENTINEL = "STOP"

class LogSystem:
    def __init__( self, workers, logs_per_worker ):
        self.workers = workers
        self.logs_per_worker = logs_per_worker
        self.queue = Queue()
      
        self.work_logger = tr.Event()
        self.ready_w = 0
        self.finished_l = 0
        self.worker_lock = tr.Lock()
        self.logger_lock = tr.Lock()
        
        


    def worker( self, worker_id, workerReady, createLog ):
        # Fill in this method.
        
        workerReady(worker_id)
        with self.worker_lock:
            self.ready_w +=1
            if self.ready_w == self.workers:
                self.work_logger.set()
        for i in range(self.logs_per_worker):
            self.queue.put(createLog(worker_id, i))
        with self.logger_lock:
            self.finished_l +=1
            if self.finished_l == self.workers:
                
                self.queue.put(SENTINEL)
            
            
   

    def logger( self, writeLog ):
        # Fill in this method.
        self.work_logger.wait()
        while True:
            get_log = self.queue.get()
            if get_log == SENTINEL:
                self.queue.task_done()
                break
            writeLog(get_log)
            self.queue.task_done()
     
    

##############################################


### Tests ####################################

def run_test( workers, logs_per_worker ):
    system = LogSystem( workers, logs_per_worker )

    ready = []
    created = []
    written = []
    check_lock = tr.Lock()

    def workerReady( worker_id ):
        time.sleep( random.random()/100 )

        with check_lock:
            assert worker_id not in ready, f"Worker {worker_id} became ready twice."
            ready.append( worker_id )

    def createLog( worker_id, log_id ):
        time.sleep( random.random()/100 )
        message = f"W{worker_id}-L{log_id}"

        with check_lock:
            created.append( message )

        return message

    def writeLog( message ):
        time.sleep( random.random()/100 )

        with check_lock:
            assert len( ready ) == workers, f"Log {message} was written before all workers were ready."
            assert message not in written, f"Log written twice: {message}"
            written.append( message )

    worker_threads = [
        tr.Thread( target=system.worker, args=(i, workerReady, createLog) )
        for i in range( workers )
    ]

    logger_thread = tr.Thread( target=system.logger, args=(writeLog,) )

    threads = worker_threads + [logger_thread]
    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in worker_threads:
        t.join( timeout=3 )

    system.queue.join()

    logger_thread.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    expected = [
        f"W{worker_id}-L{log_id}"
        for worker_id in range( workers )
        for log_id in range( logs_per_worker )
    ]

    assert sorted( ready ) == list( range( workers ) ), f"Bad ready list: {ready}"
    assert sorted( created ) == sorted( expected ), f"Bad created list: {created}"
    assert sorted( written ) == sorted( expected ), f"Bad written list: {written}"


if __name__ == "__main__":
    run_test( workers=1, logs_per_worker=10 )
    run_test( workers=2, logs_per_worker=15 )
    run_test( workers=4, logs_per_worker=20 )
    run_test( workers=6, logs_per_worker=25 )

    print( "All tests passed." )