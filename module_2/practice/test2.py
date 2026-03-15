# NB1_10_threaded.py
import threading
from queue import Queue
from math import sqrt

SENTINEL = object()

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime_after(n):
    x = n + 1
    while not is_prime(x):
        x += 1
    return x

def worker(in_q: Queue, out_q: Queue):
    lastnum = 2
    out_q.put("2 is the lowest prime number")

    while True:
        num = in_q.get()
        try:
            if num is SENTINEL:
                break

            if num <= lastnum:
                out_q.put(f"That number is smaller than {lastnum}")
                continue

            if not is_prime(num):
                out_q.put(f"{num} is not prime. Goodbye!")
                out_q.put(SENTINEL)  # tell main to stop printing/reading
                break

            # NB1_10 behavior: find the next prime bigger than num
            nxt = next_prime_after(num)
            out_q.put(f"{nxt} is prime and bigger than {num}")

            # update threshold like the original effect (after printing next prime)
            lastnum = nxt
        finally:
            in_q.task_done()

if __name__ == "__main__":
    in_q = Queue()
    out_q = Queue()

    t = threading.Thread(target=worker, args=(in_q, out_q), daemon=True)
    t.start()

    # print initial message from worker
    print(out_q.get())

    while True:
        last_prompt_hint = "2"  # prompt text doesn’t need the exact lastnum; worker enforces it
        num = int(input(f"Give me a bigger prime number bigger than {last_prompt_hint}: "))
        in_q.put(num)

        msg = out_q.get()
        if msg is SENTINEL:
            break
        print(msg)

        # worker may send extra messages (e.g., “smaller than …” then continue)
        while not out_q.empty():
            extra = out_q.get()
            if extra is SENTINEL:
                msg = SENTINEL
                break
            print(extra)
        if msg is SENTINEL:
            break

    # clean shutdown
    in_q.put(SENTINEL)
    in_q.join()
    t.join(timeout=1)