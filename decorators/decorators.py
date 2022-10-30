import functools
import time

def do_twice(func):
    
    # preserve the name and docstring of the original function
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return wrapper_do_twice


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        
        value = func(*args, **kwargs)
        
        # Do something after
        
        return value

    return wrapper_decorator
        

def timer(func):
    @functools.wraps(func)
    
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"Start Time: {start_time}")
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"End Time: {end_time}")
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    
    return wrapper_time