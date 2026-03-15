import re
import threading

class WordCounter(threading.Thread):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self.runner=False

    def count_words(self) -> int:
        words = re.findall(r"[A-Za-z]+", self.text)
        return len(words)
    def run(self):
        self.runner=self.count_words()

if __name__ == "__main__":
    texts = [
        "ERROR Disk full at /dev/sda1",
        "WARN  Connection reset by peer",
        "INFO  User logged in successfully",
        "DEBUG retrying request retrying request retrying request",
        "OK"
    ]
    expected = [6, 5, 5, 7, 1]

    threads = []
    for t in texts:
        wc = WordCounter(t)   # <-- your class
        wc.start()
        threads.append(wc)

    for wc in threads:
        wc.join()

    got = [wc.runner for wc in threads]
    print("expected:", expected)
    print("got     :", got)
    print("PASS" if got == expected else "FAIL")
    print("END")
