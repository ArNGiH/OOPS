import time
def timer(func):
    def wrapper(*args,**kwargs):
       start=time.time()
       result= func(*args,**kwargs)
       end=time.time()
       print(f"Function {func.__name__} executed in {end-start} seconds")  # Display execution time in seconds
       return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)  # Simulating a time-consuming operation


example_func(2)




