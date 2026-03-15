def make_moving_average(k):
    """
    Return a function avg(x) that stores the last k values
    and returns the current moving average.
    Raise ValueError if k <= 0.
    """
    past=[]
    def avg(a):
        if len(past) ==0 and len(past)<k:
            past.append(a)
            return a
        if len(past)>=k: past.remove(past[0])
        past.append(a)
        return sum(past)/len(past)

    return avg 

        
  

    # fill in answer here
    


# Tests
avg3 = make_moving_average(3)

print(avg3(3.0))              # 3.0
print(avg3(6.0))              # 4.5
print(avg3(9.0))              # 6.0
print(avg3(12.0))             # 9.0
print(avg3(0.0))              # 7.0

# Edge: k = 1
avg1 = make_moving_average(1)
print(avg1(10.0))             # 10.0
print(avg1(-2.5))             # -2.5

# Edge: invalid window size
try:
    make_moving_average(0)
except ValueError:
    print("ValueError")
