#!/bin/python3

import pandas

data = pandas.read_csv("weather_data.csv")
# Get data in a Column
print(data["temp"])
print(type(data))

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
# print(temp_list)

average = data["temp"].mean()
max = data["temp"].max()
min = data["temp"].min()

print(average)
print(data.condition)

# Get data in a Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")