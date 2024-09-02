import time

def cache(func):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate a long-running process
    return a + b

# First call - should take 4 seconds
start_time = time.time()
print(long_running_function(2, 3))  # Outputs: 5
print(f"First call took: {time.time() - start_time} seconds")

# Second call - should return immediately
start_time = time.time()
print(long_running_function(2, 3))  # Outputs: 5
print(f"Second call took: {time.time() - start_time} seconds")
