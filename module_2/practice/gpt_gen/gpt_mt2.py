import threading
from queue import Queue

SENTINEL = "STOP"


def produce_numbers(n, input_queue):
    for number in range(1, n + 1):
        input_queue.put(number)
    input_queue.put(SENTINEL)

def square_numbers(input_queue, output_queue):
    while True:
        item = input_queue.get()

        if item == SENTINEL:
            input_queue.task_done()
            output_queue.put(SENTINEL)
            break
        squared = item * item
        output_queue.put(squared)
        input_queue.task_done()


def collect_results(output_queue, results):
    while True:
        item = output_queue.get()
        if item == SENTINEL:
            output_queue.task_done()
            break
        results.append(item)
        output_queue.task_done()


def run_pipeline(n):
    input_queue = Queue()
    output_queue = Queue()
    results = []
    # TODO: create results list
    producer= threading.Thread(target= produce_numbers, args=(n, input_queue))
    worker = threading.Thread(target= square_numbers, args = (input_queue, output_queue))
    consumer = threading.Thread(target= collect_results, args= (output_queue, results))
    # TODO: create producer thread
    # TODO: create worker thread
    # TODO: create consumer thread
    producer.start(), worker.start(), consumer.start()
    input_queue.join()
    output_queue.join()

    producer.join()
    worker.join()
    consumer.join()
    return results

print(run_pipeline(5))