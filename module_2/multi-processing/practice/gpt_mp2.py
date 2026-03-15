import multiprocessing


def is_prime(number):
    """
    Return True if the number is prime, otherwise False.

    Guide:
    - Numbers smaller than 2 are not prime
    - Try dividing by smaller numbers
    - If any divides evenly, it is not prime
    - Otherwise it is prime
    """
    # TODO
    #print("NNN", number)
    lst=[number]
    [lst.append(b) for b in range(1,number) if number % b ==0] 
    if len(lst)<=2:
        return True
    return False
    


def find_primes(q, n):
    """
    Child process function.

    What this should do:
    - Loop from 1 to n
    - Check whether each number is prime
    - If it is prime, put it into the queue q

    Important:
    - q.put(value) adds a result into the queue
    """
    
    for b in range(2,n+1):
        if is_prime(b) == True:
            q.put(b)
    


def run_prime_search(n):
    """
    Main coordinator.

    What this should do:
    - Create the queue
    - Create the process
    - Start the process
    - Join the process
    - Pull all results from the queue into a list
    - Return the list
    """
    q = multiprocessing.Queue()

    # basic multiprocessing syntax
    p1 = multiprocessing.Process(target=find_primes, args=(q, n))
    p1.start()
    p1.join()
    results = []
    while not q.empty():
        results.append(q.get())



    return results


def run_tests():
    
    assert run_prime_search(1) == [], "Failed test: n=1"
    assert run_prime_search(2) == [2], "Failed test: n=2"
    assert run_prime_search(10) == [2, 3, 5, 7], "Failed test: n=10"
    assert run_prime_search(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Failed test: n=20"
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()