import threading
from queue import Queue


class OrderProcessor:
    SENTINEL = "STOP"

    def __init__(self, orders):
        
        self.orders = orders
        self.input_queue = Queue()
        self.output_queue = Queue()
        self.results = []
    def read_orders(self):
        for i in self.orders:
            self.input_queue.put(i)
        self.input_queue.put(OrderProcessor.SENTINEL)

    def process_orders(self):
        while True:
            item = self.input_queue.get()
            if item == OrderProcessor.SENTINEL:
                self.input_queue.task_done()
                self.output_queue.put(item)
                break
            name = item[0]
            total = item [1]
            quant = item[2]
            status = ""
            if total> 0 and quant>0:

                if total*quant >= 100:
                    status = "LARGE"
                else:
                    status = "SMALL"
                self.output_queue.put((name,total*quant,status))
         
            self.input_queue.task_done()

    def collect_results(self):
        while True:
            item = self.output_queue.get()
            if item == OrderProcessor.SENTINEL:
                self.output_queue.task_done()
                break
            self.results.append(item)
            self.output_queue.task_done()

    def run_pipeline(self):
        
        producer = threading.Thread(target=self.read_orders)
        worker = threading.Thread (target=self.process_orders)
        consumer = threading.Thread (target=self.collect_results)
        producer.start(), worker.start(), consumer.start()
        self.input_queue.join(), self.output_queue.join()
        producer.join()
        worker.join()
        consumer.join()
        return self.results

orders1 = [
    ("A101", 10, 5),
    ("A102", 0, 3),
    ("A103", 25, 4),
    ("A104", 8, 2),
    ("A105", -1, 7),
    ("A106", 50, 3)
]

orders2 = [
    ("B201", 5, 5),
    ("B202", 2, 10),
    ("B203", 1, 99)
]

orders3 = [
    ("C301", -5, 2),
    ("C302", 0, 10),
    ("C303", 8, 0)
]

processor1 = OrderProcessor(orders1)
print(processor1.run_pipeline())
# expected:
# [
#     ("A101", 50, "SMALL"),
#     ("A103", 100, "LARGE"),
#     ("A104", 16, "SMALL"),
#     ("A106", 150, "LARGE")
# ]

processor2 = OrderProcessor(orders2)
print(processor2.run_pipeline())
# expected:
# [
#     ("B201", 25, "SMALL"),
#     ("B202", 20, "SMALL"),
#     ("B203", 99, "SMALL")
# ]

processor3 = OrderProcessor(orders3)
print(processor3.run_pipeline())
# expected:
# []