from functools import reduce
#Lamda functions

some_name=lambda x,y: x*y #some name is technically not even needed, its a function that doesnt need to be asigned and will complete the opperation that is declared after the : and takes as input the x,y in this case but it can be as many/ as little inputs as i want
print(some_name(2,4))

#best example usage of this lamba function
numbers=[1,2,3,4,5,6]

squares=list(map(lambda x:x**2, numbers))
#squares= var name
# list -> Makes it return the values as a list (if list is not used u get a memory address)
#map(function, iterable) -> function is the opperation you want to do. iterable is something like a list,dictionary, tuple etc. -> it returns the operation for each value in the iterable without needing a for loop. IT DOES NOT return a LIST thats why list is needed 
print(squares)

is_even=list(filter(lambda x: x%2==0, numbers))
#is_even = var name
#list -> same as before
#filter(function, iterable) -> checks each value in the iterable to checks if it is even or not and only stores the values that are even 
print(is_even)
#example code 

result=sum(
    list(map(lambda x: x**2,#this squares all numbers that the filter allows to filter through
             filter(lambda x: x%2==0, numbers) ))) #this filters all even number
#or
result=sum(list(map(lambda x: x**2, is_even))) #This says the same thing but its using variables makes it a bit easier to read and understand 
#or
result=(sum(list(filter(lambda x: x%2==0, squares)))) #This would be the reverse process but still same output 

print(result)

vals=[(1,"fuck","hello"), (2, "hello", "Christ"), (3,"World","Jesus")]

sorts=list(sorted(vals, key=lambda x: x[1]+x[2]))
#the key=lambda x: x[1]+x[2] works like this it takes the tuple index 1,2 -? combines them ie "fuck", "hello" becomes fuckhello and then checks how high the ascii value of the first letter is and compars it to the others. Based on this it sorts the list
print(sorts)


#using reduce function
numbers=[1,2,3,4,5]
sum_of_nums=reduce(lambda acc, x: acc + x, numbers)
#reduce
#step 1: acc=1, x=2 → 2
#step 2: acc=2, x=3 → 6
#step 3: acc=6, x=4 → 24
#step 4: acc=24, x=5 → 120
#reduce essentially stores the prev opperation in this case sum in acc and does some sort of opertation on it in this case +. It always starts from the first index of the iterable

#acc= starting value it always starts at index 0 or in this case 1 
#x -> is the iterator ie the value that comes next
print(sum_of_nums)