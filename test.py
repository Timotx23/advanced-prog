import math
def turn_to_list(x):
    lst2=[x]
    [lst2.append(j) for j in range(1,x) if x%j ==0]
    return lst2
def is_primes(value):
    flst=[]
    [flst.append(b) for b in range(value) if len(turn_to_list(b))<=2 ]
    return flst


def is_prime2(i):
        if i**2 %2 !=0:
            return True
def call_prime(value):
    lst=[2]
    for i in range(2,value):
        if is_prime2(i):
             lst.append(i)
    return lst
    
    
               
        
def is_prime(number):
    lst=[]
    for i in range(1,number):
        local_lst = [i]
        for b in range(1,i):
            if i%b ==0:
                local_lst.append(i)
        if len(local_lst)<=2:
            print("Local", local_lst)
            lst.append(i)
    return lst


def filt(word):
    words= word.split("\n")
    return words
print(filt("a\nb\nc"))

