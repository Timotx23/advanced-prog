import threading

class FooBar(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.input_n = n
        self.runner = None
    def declare(self):
        ...
    def run(self):
        ...

if __name__ == "__main__":
    ...