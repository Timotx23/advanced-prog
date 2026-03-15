import threading                  # Lets us create and manage threads
from queue import Queue           # Thread-safe queue for passing data between threads
import time                       # Only used here for a tiny delay to simulate work

SENTINEL = "END"                  # Special value used to tell a thread to stop


def is_prime(n):
    """
    Check if a number is prime.
    Prime means: only divisible by 1 and itself.
    """
    if n <= 1:                    # 0, 1, and negatives are not prime
        return False

    # Check divisibility from 2 up to sqrt(n)
    # This is faster than checking all numbers up to n-1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:            # If divisible by i, then n is not prime
            return False

    return True                   # If no divisor was found, it is prime


def worker(input_queue, output_queue):
    """
    Worker thread:
    - takes numbers from input_queue
    - checks if they are prime
    - puts prime numbers into output_queue

    This thread is called a 'worker' because it does the main processing.
    """
    while True:                                   # Keep running until we receive stop signal
        number = input_queue.get()                # Take one item from the input queue
                                                  # If queue is empty, this line waits

        if number == SENTINEL:                    # If stop signal is received...
            input_queue.task_done()               # Mark this queue item as finished
            output_queue.put(SENTINEL)            # Pass stop signal to the next stage
            break                                 # Exit the loop, ending this thread

        # Simulate a little processing time so you can imagine real work happening
        time.sleep(0.1)

        if is_prime(number):                      # Do the actual computation
            output_queue.put(number)              # Send result to consumer thread

        input_queue.task_done()                   # Tell the queue this item is fully processed


def consumer(output_queue):
    """
    Consumer thread:
    - reads results from output_queue
    - prints them

    This is called a 'consumer' because it consumes processed data.
    """
    while True:                                   # Keep running until stop signal arrives
        result = output_queue.get()               # Get one processed item

        if result == SENTINEL:                    # If worker says no more results are coming...
            output_queue.task_done()              # Mark sentinel as processed
            break                                 # Exit the loop, ending this thread

        print(f"Prime found: {result}")           # Use the processed result

        output_queue.task_done()                  # Mark this result as fully handled


# ---------------- MAIN PROGRAM STARTS HERE ----------------

input_queue = Queue()                             # Queue for raw work items
output_queue = Queue()                            # Queue for processed results

# Create the worker thread
# target=worker means: when this thread starts, run worker(...)
# args=(input_queue, output_queue) are the function arguments passed into worker
worker_thread = threading.Thread(
    target=worker,
    args=(input_queue, output_queue)
)

# Create the consumer thread
# This one will run consumer(output_queue)
consumer_thread = threading.Thread(
    target=consumer,
    args=(output_queue,)
)

worker_thread.start()                             # Actually start the worker thread
consumer_thread.start()                           # Actually start the consumer thread

# Main thread now acts like the producer
# It pushes numbers into the input queue for the worker to process
for number in range(1, 31):
    input_queue.put(number)                       # Add work item to queue

# Send stop signal to worker after all numbers are added
input_queue.put(SENTINEL)

# Wait until every item placed into input_queue has been fully processed
# This includes the sentinel
input_queue.join()

# Wait until every item placed into output_queue has been fully consumed
output_queue.join()

# Wait for both threads to completely finish before ending the program
worker_thread.join()
consumer_thread.join()

print("All threads finished.")