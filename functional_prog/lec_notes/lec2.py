#Reasons to use Functions
#-> Encapsulation- Bascially a wrapper function where one doesn't need to know specifically how it works just inputs ie: map, filter, type, list etc
#-> Generalisation - changing the usefullness of a piece of code by giving it different input perameters
# -> Manageability - making code easier to read/ understand
# Maintainability - making code more understandable/ expandable
# Reusability - not having to rewrite the same line of code multiple times

#Decorators
# is a function that extends the ability of another function
def my_decorator(func):#ALWAYS get access to the function itself
    def wrapper(name):# gets access tp the input variables of the function
        print("Before the function runs...")
        enhance="Jesus " + name ##this is a very simple representation of how it can be enhanced by using the 
        result= func(enhance)#Function say_hello                    
        print("After the function runs...")
        return result
    return wrapper

@my_decorator# this calls the decorator -> if this sytax is used it wont directly start with say_hello but instead the my_decorator is called which takes the say_hello as input  BUT its only called when say_hello is being called
#Its essentially a hijacking system that allows me to not change the original function say_hello but instead leave it be and possible enhance it
def say_hello(name):
    print(f"Hello! {name}")

say_hello("Timo")

#currying/ Partial functions
#currying breaks down a single function into multiple which allows each part of the function to be very simple
#Use for modularity of code, code reusability, lazy eval, functional composition, enhanced readability (appearently)
#The good thing about currying is that it is structured u cannot do different steps at a time
#Non currying way
def not_curry(tax_rate:float, discount_amount:float, price:float) -> float:
    """This is a non currying way of how to solve the problem but the issue with this is that its not very ridgid and none expandable in the future. Example price and discount are easily mixed up and could be confused"""
    return (price - discount_amount)*(1+tax_rate)

call_not_curry= not_curry(0.25,300,500)
print(f"Version without curry: Black friday price: ${call_not_curry}")

def apply_vat(tax_rate: float) :#this is the final tax rate -> The code has a clear order first apply vat -> apply discount -> compute the final. Less risk of it being mixed up
    """This first part of the function allows the system to store the tax rate"""
    def apply_discount(discount_amount: float) :
        """This is to apply the discount"""
        def calculate_final(price: float)-> float:
            """This one does all the heavy lifting as it actually computes the final price"""
            return (price - discount_amount)*(1+tax_rate)
        return calculate_final
    return apply_discount

discount= apply_vat(0.25)
#Benifit of this system each part of the function can be held extremely simple 
#However scope is an issue as the inner functions don't have access to all the info that the outer functions have
apply_black_friday = discount(300)
apply_christmas = discount(150)
        
fridge_price: int = 500
print(f" Fridge: ${fridge_price}")
print(f"Black friday price: ${apply_black_friday(fridge_price)}") #See how the inner function can be called all day long without issues

#Partial functions
from functools import partial
def operation(x,y,z):
    return x*(y+z)
doublesum=partial(operation,2) #this is a partial function
print(doublesum(2,2))#example of a double function -> the operation function takes 3 inputs and in the doublesum i provided 2 already and now 2,2 =3 vars meaning the opperation can be done

#closures
#closures are good when you want to avoid having a global variable as this can impeed on scalability as well as it can be messed with
#IT is not currying as it doesnt break down one function with multiple inputs into different functions but instead removes the need for global vars
def enter_number_outer():
    """This functions only job is to store the global var it is not used for anything else"""
    numbers=[]
    def enter_number_inner(x: int)-> list:
        """This function takes in the actual variable and adds it to that 'global' list """
        numbers.append(x)
        print(numbers)
    return enter_number_inner
call_nums= enter_number_outer()#this calls the outer function which also has direct access to the inner function
call_nums(4)#calls the inner function
call_nums(5) 
call_nums(299)

#Iterables/ iteraters
#Iterables -> for, in, = lists, dictionaries, sets, tuples
#very simple example of creating an itterable
iterable=[1,2,3,4,5]
it = iter(iterable)#creates the thing that is iterable -> DOESN'T itterate itself
while True:
    try:
        value = next(it)#Goes through the values of each it
        
        # body
    except StopIteration:
        break
#Generators
#Benifits: can be used for infitily long sequences
#Computes only when needed -> cnstant memory doesn't suddenly require more/ less
def my_range(start, end):
    """This function will return an iterator over the given range using the yield function. It's an example of a generator function
    Generator function like this creates a __iter__() and __next__() function for me so its a lot easier and better to use then normal iterators
    """
    current=start
    while current <= end:
        yield current #This part makes it a generator function -> returns not a number but an iterator 
        current+=1
nums= my_range(1,10)
for num in nums:
    print(num)