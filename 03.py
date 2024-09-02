
def debug(func):
    def wrapper(*args, **kwargs):
       args_value=', '.join(str(arg)for arg in args)
       kwargs_value=', '.join(f"{k}={v}"  for k,v in kwargs.items())
       print(f"Calling function: {func.__name__} with arguments: {args_value} and kwargs: {kwargs_value}")
       return func(*args,**kwargs)
    return wrapper





@debug
def hello():
    print("Hello, World!")

@debug
def greet(name,greeting="Hello"):
    return print(f"{greeting}, {name}")

hello()
greet("Aryan","Hi")
