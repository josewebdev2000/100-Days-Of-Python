#!/bin/python3

class Car:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

def main():
    """Run the program as a whole."""
    
    
    print(add(2,3,4,5,6,7,8))
    print(add(2,3,45,6,7,8,5,4,3))

    print(calculate(4, add=3, multiply=5))
    
    my_car = Car(make="Nissan", model="GT-R")
    print(my_car.model)


def add(*args):
    """Return the sum of all args"""
    
    # Args IS A TUPLE
    
    sum = 0
    
    for arg in args:
        sum += arg
    
    return sum

def calculate(n, **kwargs):
    """Submit a number to different arithmetic calculations."""
    
    for key, value in kwargs.items():
        print(key)
        print(value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]


if __name__ == "__main__":
    main()