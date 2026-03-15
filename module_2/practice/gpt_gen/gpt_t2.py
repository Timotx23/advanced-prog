import math
import threading

class Stats(threading.Thread):
    def __init__(self, data: list[float]):
        super().__init__()
        self.data = data
        self.runn=()
        

    def mean(self) -> float:
        return sum(self.data) / len(self.data)

    def stdev(self) -> float:
        m = self.mean()
        var = sum((x - m) ** 2 for x in self.data) / len(self.data)
        return math.sqrt(var)
    def run(self):
        self.runn+=(self.mean(), self.stdev())
        return self.runn

if __name__ == "__main__":
    datasets = [
        [1, 1, 1, 1],          # mean=1, stdev=0
        [1, 2, 3, 4],          # mean=2.5, stdev=sqrt(1.25)=1.1180...
        [10, 10, 20, 20],      # mean=15, stdev=5
    ]
    expected = [
        (1.0, 0.0),
        (2.5, 1.1180),
        (15.0, 5.0),
    ]
    f_output=[]
    for t in datasets:
        call_stats=Stats(t)
        call_stats.start()
        f_output.append(call_stats)
    
    for call_stats in f_output:    
        call_stats.join()
    got = []
    for call_stats in f_output:
        m, s = call_stats.runn
        got.append((round(m, 4), round(s, 4)))
    print("Output", got)
    print("Expected", expected)
    if got == expected:
        print("Correct")

