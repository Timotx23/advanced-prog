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


