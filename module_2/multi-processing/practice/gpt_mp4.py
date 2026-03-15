import multiprocessing
def splitting(word):
    words = word.split("\n")
    return len(words)-1
    
def worker(task_queue, result_queue):
    """
    Repeatedly read tasks from task_queue.

    Each task is expected to be:
        (index, file_content)

    If the task is the STOP signal, terminate the worker.

    Otherwise:
        - count the number of lines in file_content
        - place (index, line_count) into result_queue
    """
    while True:
        item = task_queue.get()
        if item == "STOP":
            
            break
        index, file_content = item
        finished = splitting(file_content)
        result_queue.put((index, finished))
   


def parallel_line_count(files, num_workers=3):
    """
    Coordinator function.

    Responsibilities:
        - create the task queue and result queue
        - create worker processes
        - start all workers
        - enqueue tasks (index, file_content)
        - send STOP signals (one per worker)
        - collect results from result_queue
        - join all worker processes
        - rebuild the result list so it matches the original file order
        - return the final list
    """
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    processes = []
    for _ in range( num_workers):
        process = multiprocessing.Process(target=worker, args = (input_queue, output_queue))
        processes.append(process)
    [b.start() for b in processes]
    
    for i,file in enumerate(files):
        input_queue.put((i,file))


    for _ in range(num_workers):
        input_queue.put("STOP")
    
    results = []
    for _ in range(len(files)):
        item = output_queue.get()
        results.append(item)
    [a.join() for a in processes]
    results.sort()
    return [count for _, count in results]


def run_tests():
    assert parallel_line_count(["hello\nworld"]) == [2]
    assert parallel_line_count(["a\nb\nc", "x"]) == [3, 1]
    assert parallel_line_count(["one", "two\nthree", "four\nfive\nsix"]) == [1, 2, 3]
    assert parallel_line_count([]) == []
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()