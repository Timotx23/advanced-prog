#This is is_prime but with classes and still threading
import threading
class is_prime(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.value=number
        self.retq=False
    def turn_to_list(self,x):
        lst2=[x]
        [lst2.append(j) for j in range(1,x) if x%j ==0]
        return lst2
    def is_prime(self):
        if self.value <=1:
            return False
        return len(self.turn_to_list(self.value))<=2 
    def run(self):
        # THIS runs in the new thread
        self.retq = self.is_prime()
if __name__ == "__main__":
    prime_nums=[]
    for i in range(500):
        p=is_prime(i)
        p.start()
        p.join()
        if p.retq:
            prime_nums.append(i)
    while len(prime_nums)>0:
        print(prime_nums.pop(0))
    print("END")


