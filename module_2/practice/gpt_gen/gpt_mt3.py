import threading
from queue import Queue

SENTINEL = "STOP"


def is_prime(number):
    lst=[number]
    for b in range(1,number):
        if number%b ==0:
            lst.append(b)
    if len(lst)<=2:
        return True


def transform_prime(number):

    if number <=10:
        return number*2
    else:
       return number+100

def produce_numbers(n, input_queue):
    for i in range(1,n+1):    
        input_queue.put(i)
    input_queue.put(SENTINEL)
   


def filter_and_transform(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item == SENTINEL:
            input_queue.task_done()
            output_queue.put(SENTINEL)
            break
        if is_prime(item) == True:
            output_queue.put(transform_prime(item))
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
    input_queue= Queue ()
    output_queue = Queue ()
    results = []
    producer = threading.Thread (target=produce_numbers, args= (n, input_queue))
    worker = threading.Thread (target=filter_and_transform, args=(input_queue, output_queue))
    consumer = threading.Thread (target=collect_results, args = (output_queue, results))

    
    producer.start(), worker.start(), consumer.start()
    input_queue.join(), output_queue.join()

    producer.join()
    worker.join()
    consumer.join()
    return results
    

print(run_pipeline(1))    # expected: []
print(run_pipeline(2))    # expected: [4]
print(run_pipeline(10))   # expected: [4, 6, 10, 14]
print(run_pipeline(12))   # expected: [4, 6, 10, 14, 111]
print(run_pipeline(20))   # expected: [4, 6, 10, 14, 111, 113, 117, 119]