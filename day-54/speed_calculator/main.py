import time

def main():
    print(fast_function())
    print(slow_function())

def speed_calc_decorator(func):
    
    def wrapper():

        # get times
        time_before= time.time()
        func()
        time_after = time.time()

        time_delayed = time_before - time_after

        return f"{func.__name__} run speed: {abs(time_delayed)}s"
    
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(100000000):
        i * i

if __name__ == "__main__":
    main()