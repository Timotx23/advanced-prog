import multiprocessing
def function():
    ...
processname=...
parameters=...
p=multiprocessing.Process(target=function, name=processname, agrs=(parameters))
#start multiprocessing
p.start()
#complete the process 
p.join()
#check if process is alive
p.is_alive()
#name of process
p.name
#The current process
multiprocessing.current_process()
#How to end process
#if needed use
p.terminate or p.kill()
#one must use
if __name__ == '__main__':
    main()# or name of the function 