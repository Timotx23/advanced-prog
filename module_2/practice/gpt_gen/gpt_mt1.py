import threading
from queue import Queue

SENTINEL = "STOP"


def produce_numbers(n, input_queue):
    """
    Put all numbers from 0 to n into input_queue, then send SENTINEL.
    """
    for i in range(n+1):
        input_queue.put(i)
    input_queue.put(SENTINEL)


    

def filter_even_numbers(input_queue, output_queue):
    """
    Read items from input_queue.
    If the item is even, put it into output_queue.
    If the item is SENTINEL:
      - mark the input task as done
      - forward SENTINEL to output_queue
      - stop the thread
    """
    while True:
        number = input_queue.get() #gets each individual number
        if number == SENTINEL:
            input_queue.task_done()
            output_queue.put(SENTINEL)
            break
        if number%2 ==0:
            output_queue.put(number)
        input_queue.task_done()   


        


def collect_results(output_queue, results):
    """
    Read items from output_queue and append them to results.
    Stop when SENTINEL is received.
    """
    while True:
        numbers= output_queue.get( )
        if numbers is SENTINEL:
            output_queue.task_done()
            break
        results.append(numbers)
        output_queue.task_done()

       
      


def run_pipeline(n):
    """
    Set up queues, threads, and return the final results list.
    """
    input_queue = Queue()
    output_queue = Queue()
    results = []

    producer = threading.Thread(target=produce_numbers, args=(n, input_queue))
    worker = threading.Thread(target=filter_even_numbers, args=(input_queue, output_queue))
    consumer = threading.Thread(target=collect_results, args=(output_queue, results))

    producer.start()
    worker.start()
    consumer.start()

    # Wait until all queued tasks are processed
    input_queue.join()
    output_queue.join()

    # Wait for all threads to finish
    producer.join()
    worker.join()
    consumer.join()

    return results
running_pipeline=run_pipeline(20)
print(running_pipeline)