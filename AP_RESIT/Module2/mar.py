import threading
import time
import random
from queue import Queue


jobs = [
    ("Fix oxygen valve", 5),
    ("Restart navigation system", 3),
    ("Repair solar panel", 4),
    ("Check food supply", 1),
    ("Patch communication antenna", 2),
    ("Stabilize reactor core", 5),
    ("Clean air filters", 1),
    ("Inspect docking port", 3),
]

job_queue = Queue()
completed_jobs = []

# TODO1: create a Lock for completed_jobs
completed_jobs_lock = threading.Lock()


# TODO2: create an Event called station_ready
station_ready = threading.Event()


def engineer(engineer_id):
    # TODO3:
    # print that the engineer is waiting for station readiness
    # wait for station_ready event
    print("Engineer is waiting")
    station_ready.wait()

    while True:
        # TODO4:
        # get a job from the queue
        with completed_jobs_lock:
            job = job_queue.get()
            

            # TODO5:
            # if the job is None:
            #   mark task done
            #   print that the engineer is stopping
            #   break
            if job == None:
                
                print("Engineer is stopping")
                job_queue.task_done()
                station_ready.clear()
                break
            print(f"Engineer is working on {job[0]} with priority {job[1]}")
            

            # TODO6:
            # unpack job into job_name and priority
            # print that engineer is working on the job
            # sleep random short time

            # TODO7:
            # safely append (engineer_id, job_name, priority) to completed_jobs
            completed_jobs.append((engineer_id, job[0], job[1]))
            time.sleep(random.randint(1,5))
            job_queue.task_done()

        # TODO8:
        # mark task done
       


def main():
    # TODO9:
    # sort jobs by priority from highest to lowest
    # put them into job_queue
    lst =lambda x: x[1]
    x = sorted(jobs, key=lst, reverse= True)
    for j in x:
        job_queue.put(j)
    job_queue.put(None)
    

    engineers = []

    for i in range(4):
        # TODO10:
        # create engineer thread and append to engineers
        tr = threading.Thread(target=engineer, args=(i,))
        engineers.append(tr)
        

    for e in engineers:
        # TODO11:
        # start each engineer
        e.start()
        

    print("Station preparing systems...")
    time.sleep(2)

    # TODO12:
    # signal that station is ready
    station_ready.set()

    # TODO13:
    # add one None sentinel per engineer
    for _ in engineers:
        job_queue.put(None)
    
    

    # TODO14:
    # wait until all queue tasks are done
    station_ready.wait()

    for e in engineers:
        # TODO15:
        # join each engineer
        e.join()

    # TODO16:
    # print completed jobs sorted by priority descending
    y = lambda a: a[1]
    print(sorted(completed_jobs, key= y))


if __name__ == "__main__":
    main()