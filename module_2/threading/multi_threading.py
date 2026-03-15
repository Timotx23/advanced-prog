import threading
def function():
    ...
threadname="Some imaginary universe"
parameters="Some imaginary parameters"
t=threading.Thread(target= function, name=threadname, args=(parameters))
t.start()#Starts the thread
t.join() #Completes the thread by "closing" it
t.is_alive() # checks if the thread is alive
t.name #checks the name of the thread
threading.current_thread()# checks if the current thread can be found
threading.enumerate()# lists all of the threads that where found
#