from multiprocessing import Process, Queue
SENTINAL = "STOP"

def worker(task_queue, result_queue):
    """
    Worker process logic.

    What this function should do:
    1. Repeatedly pull items from task_queue.
    2. If the item is the stop signal, exit the loop.
    3. Otherwise, process the item.
       - For this problem, processing means squaring the number.
    4. Put the processed result into result_queue.

    Important idea:
    - This function should keep running until it receives a stop signal.
    - Think of it like a mini service that waits for work.
    """
    # TODO:
    # - Start an infinite loop
    # - Read one task from the task_queue
    # - Check whether it is the stop signal
    # - If it is, stop the worker
    # - Otherwise compute the square
    # - Put the result in result_queue
    while True:
        item = task_queue.get()
        if item  == SENTINAL:
            break
        result_queue.put(item*item)
    




def start_workers(num_workers, task_queue, result_queue):
    """
    Create and start worker processes.

    What this function should do:
    1. Create exactly num_workers Process objects.
    2. Each Process should target the worker function.
    3. Pass the queues as arguments.
    4. Start each process.
    5. Return the list of created processes.

    Important idea:
    - You need the returned list later so you can join the processes.
    """
    # TODO:
    # - Make an empty list to store process objects
    # - Loop num_workers times
    # - Create a Process for each worker
    # - Start it
    # - Save it in the list
    # - Return the list
    results = []
    for _ in range(num_workers):
        process = Process(target=worker, args=(task_queue, result_queue))
        process.start()
        results.append(process)
    return results




def enqueue_tasks(orders, task_queue):
    """
    Put all orders into the task queue.

    What this function should do:
    1. Loop through the input orders.
    2. Put each order into task_queue.

    Important idea:
    - This is the producer side of the pipeline.
    """
    # TODO:
    # - For each order, push it into the task_queue
    for b in orders:
        task_queue.put(b)
    return task_queue


def stop_workers(num_workers, task_queue):
    """
    Send stop signals so workers know when to exit.

    What this function should do:
    1. Put one stop signal into task_queue for each worker.

    Important idea:
    - If you have 3 workers, you need 3 stop signals.
    - Otherwise some workers may keep waiting forever.
    """
    # TODO:
    # - Add one stop signal per worker into the queue
    for b in range(num_workers):
        task_queue.put(SENTINAL)
    return task_queue
  


def collect_results(num_tasks, result_queue):
    """
    Collect all processed results.

    What this function should do:
    1. Pull exactly num_tasks results from result_queue.
    2. Store them in a list.
    3. Return that list.

    Important idea:
    - You know how many results to expect because you know
      how many input tasks you sent.
    """
    # TODO:
    # - Make a results list
    # - Read exactly num_tasks items from result_queue
    # - Return the list
    results  = []
    
    
    for b in range(num_tasks):
        item = result_queue.get()
        results.append(item)
    return results
    


def join_workers(processes):
    """
    Wait for all worker processes to finish.

    What this function should do:
    1. Loop through every process object.
    2. Join each one.

    Important idea:
    - Joining ensures the main program waits until workers are done.
    """
    # TODO:
    # - Join each process
    for b in processes:
        b.join()
    
def parallel_process_orders(orders, num_workers):
    """
    Main coordinator function.

    What this function should do:
    1. Create the task queue and result queue.
    2. Start the worker processes.
    3. Enqueue all tasks.
    4. Send stop signals.
    5. Collect all results.
    6. Join all workers.
    7. Return the sorted results.

    Important idea:
    - The order in which results come back may not match input order.
    - That is why the final answer should be sorted before returning.
    """
    # TODO:
    input_queue = Queue ()
    output_queue = Queue ()

    # - Create both queues
    # - Start workers
    # - Enqueue tasks
    # - Stop workers
    # - Collect results
    # - Join workers
    # - Return sorted results


    worker_proccess = start_workers(num_workers, input_queue, output_queue)
    enqueue_tasks(orders, input_queue)
    stop_workers(num_workers, input_queue)
    results = collect_results(len(orders), output_queue)
    join_workers(worker_proccess)
    return sorted(results)
    
def run_tests():
    # Test 1: basic example
    orders = [2, 4, 6, 8]
    expected = [4, 16, 36, 64]
    result = parallel_process_orders(orders, 2)
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"

    # Test 2: single worker
    orders = [1, 3, 5]
    expected = [1, 9, 25]
    result = parallel_process_orders(orders, 1)
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"

    # Test 3: more workers than tasks
    orders = [7, 2]
    expected = [4, 49]
    result = parallel_process_orders(orders, 4)
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"

    # Test 4: empty input
    orders = []
    expected = []
    result = parallel_process_orders(orders, 2)
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"

    # Test 5: includes zero
    orders = [0, 2, 10]
    expected = [0, 4, 100]
    result = parallel_process_orders(orders, 3)
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()