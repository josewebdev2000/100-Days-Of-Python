#!/bin/python3

with open("../../../../my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file_2.txt", "w") as file:
    file.write("I shall enter the real of pure humanity.")
