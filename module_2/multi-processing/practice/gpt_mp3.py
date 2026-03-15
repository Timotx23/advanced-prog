import multiprocessing
import multiprocessing.process


def worker(task_queue, result_queue):
    while True:
        number = task_queue.get()

        if number == "STOP":
            break
        result_queue.put(number*number)


        # TODO
        # compute the square of number
        # put result into result_queue


def run_parallel_square(n, num_workers=2):

    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    processes = []


    for _ in range(num_workers): 
        process = multiprocessing.Process(target = worker, args=(task_queue, result_queue))
        processes.append(process)

    #starts all of the processes inside of the processes list
    [p.start() for p in processes]
    
    # add tasks to queue
    for i in range(1, n + 1):
        task_queue.put(i)

    # send stop signal for each worker
    for _ in range(num_workers):
        task_queue.put("STOP")

    # TODO
    # collect results from result_queue
    results = []
    for i in range(n):
        item = result_queue.get()
        results.append(item)
    [ps.join() for ps in processes]
    return sorted(results)


if __name__ == '__main__':
    print(run_parallel_square(5))
    print(run_parallel_square(10))