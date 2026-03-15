import threading
from queue import Queue

SENTINEL = "STOP"


     
def read_logs(logs, input_queue):
    for i in logs:
        input_queue.put(i)
    input_queue.put(SENTINEL)


def parse_errors(input_queue, output_queue):
    while True:
        inpu = input_queue.get()
        if inpu == SENTINEL:
            input_queue.task_done()
            output_queue.put(SENTINEL)
            break
        tipe,message = inpu.split(":")
        if tipe == "ERROR":
            output_queue.put((tipe, len(message.strip())))
        input_queue.task_done()
        


def collect_parsed(output_queue, results):
    while True:
        inpu = output_queue.get()
        if inpu == SENTINEL:
            output_queue.task_done()
            break
        results.append(inpu)
        output_queue.task_done()


def run_pipeline(logs):
    input_queue = Queue ()
    output_queue = Queue ()
    results = []
    reader_thread = threading.Thread(target=read_logs, args=(logs, input_queue))
    worker = threading.Thread(target=(parse_errors), args= (input_queue, output_queue))
    consumer = threading.Thread(target=(collect_parsed), args=(output_queue, results))
    reader_thread.start(), worker.start(), consumer.start()
    input_queue.join(), output_queue.join()
    reader_thread.join()
    worker.join()
    consumer.join()
    return results


logs1 = [
    "INFO: System started",
    "ERROR: Disk failure",
    "WARN: Temperature high",
    "ERROR: Connection lost"
]
print(run_pipeline(logs1))
# expected: [("ERROR", 12), ("ERROR", 15)]

logs2 = [
    "INFO: Boot",
    "INFO: Ready",
    "WARN: Low memory"
]
print(run_pipeline(logs2))
# expected: []

logs3 = [
    "ERROR: A",
    "ERROR: BB",
    "ERROR: CCC"
]
print(run_pipeline(logs3))
# expected: [("ERROR", 1), ("ERROR", 2), ("ERROR", 3)]