# NB2_17.py

import threading as tr, time, random

### Exercise 15 ##############################
# Context:
# A program needs to check many student submissions at the same time.
#
# Each submission has:
# - a student name
# - a list of test results: True means passed, False means failed
#
# Each submission must be checked in its own thread.
#
# Your job is to fill in the SubmissionChecker class.
#
# Requirements:
# - SubmissionChecker must inherit from threading.Thread.
# - Each thread must calculate its own score.
# - The score is the number of passed tests.
# - The result must be stored inside the thread object.
# - The main program must be able to read the result after join().
# - The program must not use global variables.
#
# You may edit only the SubmissionChecker class.
# Do not edit the tests.

class SubmissionChecker(tr.Thread):
    def __init__( self, student_name: str, tests:list ):
        # Fill in this method.
        self.student_name = student_name
        self.tests = tests
        self.score = 0
        super().__init__()
        
     
    def run( self ):
        # Fill in this method.
        self.score = len([i for i in self.tests if i == True])
        return self.score

##############################################


### Tests ####################################

def run_test( submissions ):
    threads = []

    for student_name, tests in submissions:
        t = SubmissionChecker( student_name, tests )
        threads.append( t )

    random.shuffle( threads )

    for t in threads:
        t.start()

    for t in threads:
        t.join( timeout=3 )

    for t in threads:
        assert not t.is_alive(), "A thread did not finish."

    results = {}

    for t in threads:
        results[t.student_name] = t.score

    expected = {
        student_name: sum( tests )
        for student_name, tests in submissions
    }

    assert results == expected, f"Expected {expected}, but got {results}"


if __name__ == "__main__":
    run_test([
        ("Alice", [True, True, False, True]),
        ("Bob", [False, False, True]),
        ("Charlie", [True, True, True, True])
    ])

    run_test([
        ("Dina", [random.choice([True, False]) for _ in range(100)]),
        ("Eli", [random.choice([True, False]) for _ in range(100)]),
        ("Fatima", [random.choice([True, False]) for _ in range(100)]),
        ("Gus", [random.choice([True, False]) for _ in range(100)])
    ])

    run_test([
        (f"Student{i}", [random.choice([True, False]) for _ in range(50)])
        for i in range(25)
    ])

    print( "All tests passed." )